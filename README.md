# AI Intelligence System (AI情报系统)

一个基于人工智能的情报分析系统，提供智能化的信息处理、分析和洞察功能。

## 系统架构

- **后端**: Python + FastAPI + SQLite
- **前端**: React + TypeScript + Ant Design
- **AI引擎**: Claude API / OpenAI API
- **部署**: 单机版（可扩展至分布式）

## 核心功能

### 1. AI智能分析
- 文本情报智能分析
- 实体识别与关系提取
- 情感分析与倾向判断
- 关键信息摘要生成
- 趋势预测与风险评估

### 2. 情报管理
- 情报数据的增删改查
- 多维度分类和标签
- 历史记录追踪
- 批量导入导出

### 3. 可视化展示
- 分析结果可视化
- 数据图表展示
- 关系网络图谱
- 实时统计面板

## 快速开始

### 环境要求

- Python 3.9+
- Node.js 18+
- npm 或 yarn

### 后端设置

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，添加 API 密钥

# 初始化数据库
python -m app.db.init_db

# 启动服务器
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 前端设置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

访问 http://localhost:5173 查看前端应用
访问 http://localhost:8000/docs 查看API文档

## 项目结构

```
.
├── backend/                 # 后端代码
│   ├── app/
│   │   ├── api/            # API路由
│   │   ├── core/           # 核心配置
│   │   ├── models/         # 数据模型
│   │   ├── services/       # 业务逻辑
│   │   ├── db/             # 数据库
│   │   └── main.py         # 应用入口
│   ├── tests/              # 测试
│   └── requirements.txt    # Python依赖
│
├── frontend/               # 前端代码
│   ├── src/
│   │   ├── components/    # React组件
│   │   ├── pages/         # 页面
│   │   ├── services/      # API服务
│   │   ├── types/         # TypeScript类型
│   │   └── App.tsx        # 应用入口
│   └── package.json       # Node依赖
│
├── docs/                  # 文档
├── scripts/               # 脚本工具
└── README.md             # 项目说明
```

## API文档

启动后端服务后，访问以下地址查看完整API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 主要API端点

- `POST /api/intelligence/analyze` - 提交情报进行AI分析
- `GET /api/intelligence/{id}` - 获取情报详情
- `GET /api/intelligence/` - 获取情报列表
- `POST /api/intelligence/` - 创建新情报
- `GET /api/analysis/{id}` - 获取分析结果

## 配置说明

### 环境变量

在 `backend/.env` 文件中配置：

```env
# API密钥
ANTHROPIC_API_KEY=your_claude_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# 数据库
DATABASE_URL=sqlite:///./intelligence.db

# 应用配置
APP_NAME=AI Intelligence System
DEBUG=True
SECRET_KEY=your-secret-key-here
```

## 开发指南

### 添加新的分析功能

1. 在 `backend/app/services/ai_service.py` 中添加分析方法
2. 在 `backend/app/api/intelligence.py` 中创建API端点
3. 在前端 `frontend/src/services/api.ts` 中添加API调用
4. 在前端创建对应的UI组件

### 数据库迁移

```bash
cd backend
# 创建迁移
alembic revision --autogenerate -m "description"
# 应用迁移
alembic upgrade head
```

## 测试

```bash
# 后端测试
cd backend
pytest

# 前端测试
cd frontend
npm test
```

## 生产部署

### 使用Docker

```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d
```

### 手动部署

参见 `docs/deployment.md`

## 安全性

- API密钥通过环境变量管理，不要提交到代码库
- 敏感数据加密存储
- API请求使用CORS保护
- 输入数据进行验证和清理

## 性能优化

- 数据库查询优化和索引
- API响应缓存
- 前端代码分割和懒加载
- 静态资源CDN加速

## 故障排除

### 常见问题

1. **API连接失败**
   - 检查环境变量中的API密钥是否正确
   - 确认网络连接正常

2. **数据库错误**
   - 运行数据库迁移：`alembic upgrade head`
   - 检查数据库文件权限

3. **前端无法连接后端**
   - 确认后端服务已启动
   - 检查CORS配置

## 贡献指南

欢迎贡献！请阅读 `CONTRIBUTING.md` 了解详情。

## 许可证

MIT License

## 联系方式

- 问题反馈: [GitHub Issues](https://github.com/your-repo/issues)
- 文档: [Wiki](https://github.com/your-repo/wiki)

## 更新日志

查看 `CHANGELOG.md` 了解版本更新历史。
