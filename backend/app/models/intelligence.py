from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, Enum
from sqlalchemy.sql import func
import enum
from ..db.database import Base


class IntelligenceStatus(str, enum.Enum):
    """情报状态枚举"""
    PENDING = "pending"  # 待分析
    ANALYZING = "analyzing"  # 分析中
    COMPLETED = "completed"  # 已完成
    FAILED = "failed"  # 分析失败


class IntelligenceType(str, enum.Enum):
    """情报类型枚举"""
    TEXT = "text"  # 文本情报
    NEWS = "news"  # 新闻情报
    REPORT = "report"  # 报告情报
    SOCIAL_MEDIA = "social_media"  # 社交媒体
    OTHER = "other"  # 其他


class Intelligence(Base):
    """情报数据模型"""
    __tablename__ = "intelligences"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=True)
    type = Column(Enum(IntelligenceType), default=IntelligenceType.TEXT)
    status = Column(Enum(IntelligenceStatus), default=IntelligenceStatus.PENDING)

    # 元数据
    tags = Column(JSON, default=list)  # 标签列表
    metadata = Column(JSON, default=dict)  # 额外元数据

    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Intelligence {self.id}: {self.title}>"


class Analysis(Base):
    """AI分析结果模型"""
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    intelligence_id = Column(Integer, nullable=False, index=True)

    # 分析结果
    summary = Column(Text)  # 摘要
    sentiment = Column(String(50))  # 情感分析: positive, negative, neutral
    sentiment_score = Column(Integer)  # 情感得分 -100 到 100
    entities = Column(JSON, default=list)  # 实体识别结果
    keywords = Column(JSON, default=list)  # 关键词
    topics = Column(JSON, default=list)  # 主题
    risk_level = Column(String(50))  # 风险等级: low, medium, high, critical
    insights = Column(Text)  # AI洞察
    full_analysis = Column(Text)  # 完整分析文本

    # AI模型信息
    model_used = Column(String(100))  # 使用的模型
    analysis_duration = Column(Integer)  # 分析耗时(秒)

    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Analysis {self.id} for Intelligence {self.intelligence_id}>"
