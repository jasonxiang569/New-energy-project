from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..models.schemas import StatsResponse
from ..services.intelligence_service import StatsService

router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.get("/", response_model=StatsResponse)
async def get_stats(db: Session = Depends(get_db)):
    """获取系统统计数据"""
    return StatsService.get_stats(db)
