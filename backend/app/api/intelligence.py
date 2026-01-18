from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from ..db.database import get_db
from ..models import (
    IntelligenceCreate,
    IntelligenceUpdate,
    IntelligenceResponse,
    IntelligenceListResponse,
    AnalysisRequest,
    AnalysisResponse,
    QuickAnalysisRequest,
    QuickAnalysisResponse,
    IntelligenceStatus,
    IntelligenceType,
)
from ..services.intelligence_service import IntelligenceService, AnalysisService
from ..services.ai_service import ai_service

router = APIRouter(prefix="/api/intelligence", tags=["intelligence"])


@router.post("/", response_model=IntelligenceResponse, status_code=201)
async def create_intelligence(
    intelligence: IntelligenceCreate,
    db: Session = Depends(get_db)
):
    """创建新情报"""
    return IntelligenceService.create_intelligence(db, intelligence)


@router.get("/{intelligence_id}", response_model=IntelligenceResponse)
async def get_intelligence(
    intelligence_id: int,
    db: Session = Depends(get_db)
):
    """获取情报详情"""
    intelligence = IntelligenceService.get_intelligence(db, intelligence_id)
    if not intelligence:
        raise HTTPException(status_code=404, detail="Intelligence not found")
    return intelligence


@router.get("/", response_model=IntelligenceListResponse)
async def list_intelligences(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: Optional[IntelligenceStatus] = None,
    type: Optional[IntelligenceType] = None,
    db: Session = Depends(get_db)
):
    """获取情报列表"""
    items, total = IntelligenceService.get_intelligences(db, skip, limit, status, type)
    return {"total": total, "items": items}


@router.put("/{intelligence_id}", response_model=IntelligenceResponse)
async def update_intelligence(
    intelligence_id: int,
    intelligence_update: IntelligenceUpdate,
    db: Session = Depends(get_db)
):
    """更新情报"""
    intelligence = IntelligenceService.update_intelligence(db, intelligence_id, intelligence_update)
    if not intelligence:
        raise HTTPException(status_code=404, detail="Intelligence not found")
    return intelligence


@router.delete("/{intelligence_id}", status_code=204)
async def delete_intelligence(
    intelligence_id: int,
    db: Session = Depends(get_db)
):
    """删除情报"""
    success = IntelligenceService.delete_intelligence(db, intelligence_id)
    if not success:
        raise HTTPException(status_code=404, detail="Intelligence not found")


@router.post("/{intelligence_id}/analyze", response_model=AnalysisResponse)
async def analyze_intelligence(
    intelligence_id: int,
    request: Optional[AnalysisRequest] = None,
    db: Session = Depends(get_db)
):
    """对情报进行AI分析"""
    # 获取情报
    intelligence = IntelligenceService.get_intelligence(db, intelligence_id)
    if not intelligence:
        raise HTTPException(status_code=404, detail="Intelligence not found")

    # 更新状态为分析中
    IntelligenceService.update_status(db, intelligence_id, IntelligenceStatus.ANALYZING)

    try:
        # 执行AI分析
        model = request.model if request else None
        analysis_result = await ai_service.analyze_intelligence(intelligence.content, model)

        # 保存分析结果
        db_analysis = AnalysisService.create_analysis(db, intelligence_id, analysis_result)

        # 更新情报状态为已完成
        IntelligenceService.update_status(db, intelligence_id, IntelligenceStatus.COMPLETED)

        return db_analysis

    except Exception as e:
        # 更新状态为失败
        IntelligenceService.update_status(db, intelligence_id, IntelligenceStatus.FAILED)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@router.get("/{intelligence_id}/analyses", response_model=list[AnalysisResponse])
async def get_intelligence_analyses(
    intelligence_id: int,
    db: Session = Depends(get_db)
):
    """获取情报的所有分析结果"""
    intelligence = IntelligenceService.get_intelligence(db, intelligence_id)
    if not intelligence:
        raise HTTPException(status_code=404, detail="Intelligence not found")

    analyses = AnalysisService.get_analyses_by_intelligence(db, intelligence_id)
    return analyses


@router.post("/quick-analyze", response_model=QuickAnalysisResponse)
async def quick_analyze(request: QuickAnalysisRequest):
    """快速分析（不保存到数据库）"""
    try:
        result = await ai_service.analyze_intelligence(request.content, request.model)
        return {
            "summary": result.get("summary", ""),
            "sentiment": result.get("sentiment", "neutral"),
            "sentiment_score": result.get("sentiment_score", 0),
            "entities": result.get("entities", []),
            "keywords": result.get("keywords", []),
            "topics": result.get("topics", []),
            "risk_level": result.get("risk_level", "low"),
            "insights": result.get("insights", ""),
            "full_analysis": result.get("full_analysis", "")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
