from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..models.intelligence import Intelligence, Analysis, IntelligenceStatus, IntelligenceType
from ..models.schemas import IntelligenceCreate, IntelligenceUpdate


class IntelligenceService:
    """情报数据服务"""

    @staticmethod
    def create_intelligence(db: Session, intelligence: IntelligenceCreate) -> Intelligence:
        """创建新情报"""
        db_intelligence = Intelligence(
            title=intelligence.title,
            content=intelligence.content,
            source=intelligence.source,
            type=intelligence.type,
            tags=intelligence.tags,
            metadata=intelligence.metadata,
            status=IntelligenceStatus.PENDING
        )
        db.add(db_intelligence)
        db.commit()
        db.refresh(db_intelligence)
        return db_intelligence

    @staticmethod
    def get_intelligence(db: Session, intelligence_id: int) -> Optional[Intelligence]:
        """获取单个情报"""
        return db.query(Intelligence).filter(Intelligence.id == intelligence_id).first()

    @staticmethod
    def get_intelligences(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        status: Optional[IntelligenceStatus] = None,
        type: Optional[IntelligenceType] = None
    ) -> tuple[List[Intelligence], int]:
        """获取情报列表"""
        query = db.query(Intelligence)

        if status:
            query = query.filter(Intelligence.status == status)
        if type:
            query = query.filter(Intelligence.type == type)

        total = query.count()
        items = query.order_by(desc(Intelligence.created_at)).offset(skip).limit(limit).all()

        return items, total

    @staticmethod
    def update_intelligence(
        db: Session,
        intelligence_id: int,
        intelligence_update: IntelligenceUpdate
    ) -> Optional[Intelligence]:
        """更新情报"""
        db_intelligence = IntelligenceService.get_intelligence(db, intelligence_id)
        if not db_intelligence:
            return None

        update_data = intelligence_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_intelligence, field, value)

        db.commit()
        db.refresh(db_intelligence)
        return db_intelligence

    @staticmethod
    def delete_intelligence(db: Session, intelligence_id: int) -> bool:
        """删除情报"""
        db_intelligence = IntelligenceService.get_intelligence(db, intelligence_id)
        if not db_intelligence:
            return False

        # 同时删除相关分析
        db.query(Analysis).filter(Analysis.intelligence_id == intelligence_id).delete()
        db.delete(db_intelligence)
        db.commit()
        return True

    @staticmethod
    def update_status(db: Session, intelligence_id: int, status: IntelligenceStatus) -> Optional[Intelligence]:
        """更新情报状态"""
        db_intelligence = IntelligenceService.get_intelligence(db, intelligence_id)
        if not db_intelligence:
            return None

        db_intelligence.status = status
        db.commit()
        db.refresh(db_intelligence)
        return db_intelligence


class AnalysisService:
    """分析结果服务"""

    @staticmethod
    def create_analysis(db: Session, intelligence_id: int, analysis_data: dict) -> Analysis:
        """创建分析结果"""
        db_analysis = Analysis(
            intelligence_id=intelligence_id,
            summary=analysis_data.get("summary"),
            sentiment=analysis_data.get("sentiment"),
            sentiment_score=analysis_data.get("sentiment_score"),
            entities=analysis_data.get("entities", []),
            keywords=analysis_data.get("keywords", []),
            topics=analysis_data.get("topics", []),
            risk_level=analysis_data.get("risk_level"),
            insights=analysis_data.get("insights"),
            full_analysis=analysis_data.get("full_analysis"),
            model_used=analysis_data.get("model_used"),
            analysis_duration=analysis_data.get("analysis_duration")
        )
        db.add(db_analysis)
        db.commit()
        db.refresh(db_analysis)
        return db_analysis

    @staticmethod
    def get_analysis(db: Session, analysis_id: int) -> Optional[Analysis]:
        """获取单个分析结果"""
        return db.query(Analysis).filter(Analysis.id == analysis_id).first()

    @staticmethod
    def get_analyses_by_intelligence(db: Session, intelligence_id: int) -> List[Analysis]:
        """获取某个情报的所有分析结果"""
        return db.query(Analysis).filter(
            Analysis.intelligence_id == intelligence_id
        ).order_by(desc(Analysis.created_at)).all()

    @staticmethod
    def get_latest_analysis(db: Session, intelligence_id: int) -> Optional[Analysis]:
        """获取某个情报的最新分析结果"""
        return db.query(Analysis).filter(
            Analysis.intelligence_id == intelligence_id
        ).order_by(desc(Analysis.created_at)).first()


class StatsService:
    """统计服务"""

    @staticmethod
    def get_stats(db: Session) -> dict:
        """获取系统统计数据"""
        # 情报统计
        total_intelligences = db.query(Intelligence).count()
        pending = db.query(Intelligence).filter(Intelligence.status == IntelligenceStatus.PENDING).count()
        analyzing = db.query(Intelligence).filter(Intelligence.status == IntelligenceStatus.ANALYZING).count()
        completed = db.query(Intelligence).filter(Intelligence.status == IntelligenceStatus.COMPLETED).count()
        failed = db.query(Intelligence).filter(Intelligence.status == IntelligenceStatus.FAILED).count()

        # 分析统计
        total_analyses = db.query(Analysis).count()

        # 按类型统计
        by_type = {}
        for type in IntelligenceType:
            count = db.query(Intelligence).filter(Intelligence.type == type).count()
            by_type[type.value] = count

        # 按情感统计
        sentiment_stats = db.query(
            Analysis.sentiment, func.count(Analysis.id)
        ).group_by(Analysis.sentiment).all()
        by_sentiment = {sentiment: count for sentiment, count in sentiment_stats}

        # 按风险等级统计
        risk_stats = db.query(
            Analysis.risk_level, func.count(Analysis.id)
        ).group_by(Analysis.risk_level).all()
        by_risk_level = {risk: count for risk, count in risk_stats}

        return {
            "total_intelligences": total_intelligences,
            "pending": pending,
            "analyzing": analyzing,
            "completed": completed,
            "failed": failed,
            "total_analyses": total_analyses,
            "by_type": by_type,
            "by_sentiment": by_sentiment,
            "by_risk_level": by_risk_level
        }
