from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .db.database import init_db
from .api import intelligence, stats

# 创建FastAPI应用
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="AI Intelligence Analysis System - 智能情报分析系统",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(intelligence.router)
app.include_router(stats.router)


@app.on_event("startup")
async def startup_event():
    """应用启动时初始化数据库"""
    init_db()
    print(f"🚀 {settings.APP_NAME} v{settings.VERSION} started successfully!")
    print(f"📚 API文档: http://localhost:8000/docs")
    print(f"🔧 调试模式: {settings.DEBUG}")


@app.get("/")
async def root():
    """根路径"""
    return {
        "name": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}
