"""
数据库初始化脚本
运行: python -m app.db.init_db
"""
from .database import init_db, engine
from ..models.intelligence import Base


def main():
    """初始化数据库"""
    print("正在创建数据库表...")
    init_db()
    print("✅ 数据库初始化完成！")
    print(f"数据库位置: {engine.url}")


if __name__ == "__main__":
    main()
