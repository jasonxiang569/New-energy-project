from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from .intelligence import IntelligenceStatus, IntelligenceType


# Intelligence Schemas
class IntelligenceBase(BaseModel):
    """情报基础模型"""
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)
    source: Optional[str] = None
    type: IntelligenceType = IntelligenceType.TEXT
    tags: List[str] = []
    metadata: Dict[str, Any] = {}


class IntelligenceCreate(IntelligenceBase):
    """创建情报请求模型"""
    pass


class IntelligenceUpdate(BaseModel):
    """更新情报请求模型"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    content: Optional[str] = Field(None, min_length=1)
    source: Optional[str] = None
    type: Optional[IntelligenceType] = None
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    status: Optional[IntelligenceStatus] = None


class IntelligenceResponse(IntelligenceBase):
    """情报响应模型"""
    id: int
    status: IntelligenceStatus
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class IntelligenceListResponse(BaseModel):
    """情报列表响应"""
    total: int
    items: List[IntelligenceResponse]


# Analysis Schemas
class AnalysisRequest(BaseModel):
    """分析请求模型"""
    intelligence_id: int
    model: Optional[str] = None


class AnalysisResponse(BaseModel):
    """分析结果响应模型"""
    id: int
    intelligence_id: int
    summary: Optional[str] = None
    sentiment: Optional[str] = None
    sentiment_score: Optional[int] = None
    entities: List[Dict[str, Any]] = []
    keywords: List[str] = []
    topics: List[str] = []
    risk_level: Optional[str] = None
    insights: Optional[str] = None
    full_analysis: Optional[str] = None
    model_used: Optional[str] = None
    analysis_duration: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Quick Analysis (without saving to DB)
class QuickAnalysisRequest(BaseModel):
    """快速分析请求（不保存到数据库）"""
    content: str = Field(..., min_length=1)
    model: Optional[str] = None


class QuickAnalysisResponse(BaseModel):
    """快速分析响应"""
    summary: str
    sentiment: str
    sentiment_score: int
    entities: List[Dict[str, Any]]
    keywords: List[str]
    topics: List[str]
    risk_level: str
    insights: str
    full_analysis: str


# Stats
class StatsResponse(BaseModel):
    """统计数据响应"""
    total_intelligences: int
    pending: int
    analyzing: int
    completed: int
    failed: int
    total_analyses: int
    by_type: Dict[str, int]
    by_sentiment: Dict[str, int]
    by_risk_level: Dict[str, int]
