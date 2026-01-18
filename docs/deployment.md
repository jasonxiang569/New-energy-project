# 部署指南

## 系统要求

- Python 3.9 或更高版本
- Node.js 18 或更高版本
- SQLite（已包含在Python中）

## 快速部署

### 1. 克隆项目

```bash
git clone <repository-url>
cd New-energy-project
```

### 2. 后端部署

```bash
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，添加你的 Anthropic API Key
nano .env  # 或使用其他编辑器

# 初始化数据库
python -m app.db.init_db

# 启动后端服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

后端服务将在 http://localhost:8000 启动

### 3. 前端部署

打开新的终端窗口：

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端应用将在 http://localhost:5173 启动

## 生产环境部署

### 使用 Docker Compose

创建 `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - DATABASE_URL=sqlite:///./data/intelligence.db
    volumes:
      - ./data:/app/data
    restart: unless-stopped

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: unless-stopped
```

启动服务：

```bash
docker-compose up -d
```

### 手动生产部署

#### 后端

```bash
cd backend

# 安装生产依赖
pip install -r requirements.txt gunicorn

# 使用 Gunicorn 启动
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

#### 前端

```bash
cd frontend

# 构建生产版本
npm run build

# 使用 Nginx 或其他 Web 服务器部署 dist 目录
```

## 配置说明

### 环境变量

在 `backend/.env` 中配置：

```env
# 必需: Anthropic API Key
ANTHROPIC_API_KEY=sk-ant-xxx

# 可选: OpenAI API Key (如果要使用OpenAI模型)
OPENAI_API_KEY=sk-xxx

# 数据库URL
DATABASE_URL=sqlite:///./intelligence.db

# 应用配置
APP_NAME=AI Intelligence System
DEBUG=False  # 生产环境设为False
SECRET_KEY=your-very-secure-secret-key-here

# CORS设置
CORS_ORIGINS=http://localhost:5173,http://localhost:3000,https://your-domain.com

# AI模型设置
DEFAULT_AI_MODEL=claude-3-sonnet-20240229
MAX_ANALYSIS_LENGTH=10000
```

### Nginx 配置示例

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # 前端
    location / {
        root /path/to/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # 后端 API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # API文档
    location /docs {
        proxy_pass http://localhost:8000;
    }
}
```

## 数据备份

### 备份数据库

```bash
cp backend/intelligence.db backup/intelligence_$(date +%Y%m%d_%H%M%S).db
```

### 恢复数据库

```bash
cp backup/intelligence_20240117_120000.db backend/intelligence.db
```

## 监控和日志

### 查看后端日志

```bash
# 如果使用 systemd
journalctl -u ai-intelligence-backend -f

# 如果使用 Docker
docker logs -f ai-intelligence-backend
```

### 健康检查

```bash
# 检查后端健康状态
curl http://localhost:8000/health

# 检查前端
curl http://localhost:5173
```

## 故障排除

### 常见问题

1. **端口被占用**
   ```bash
   # 查找占用端口的进程
   lsof -i :8000
   # 杀死进程
   kill -9 <PID>
   ```

2. **数据库权限问题**
   ```bash
   # 给数据库文件正确的权限
   chmod 644 backend/intelligence.db
   ```

3. **API Key 无效**
   - 检查 .env 文件中的 API Key 是否正确
   - 确认 API Key 有足够的配额

4. **CORS 错误**
   - 检查后端 .env 中的 CORS_ORIGINS 设置
   - 确保前端URL在允许列表中

## 性能优化

### 后端优化

1. 使用多个 worker:
   ```bash
   gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. 启用缓存（Redis）

3. 数据库索引优化

### 前端优化

1. 启用 gzip 压缩
2. 配置 CDN
3. 代码分割和懒加载

## 安全建议

1. **HTTPS**: 生产环境必须使用 HTTPS
2. **防火墙**: 只开放必要的端口
3. **定期更新**: 保持依赖包最新
4. **密钥管理**: 使用环境变量或密钥管理服务
5. **访问控制**: 实现用户认证和授权
6. **速率限制**: 防止API滥用
7. **日志审计**: 记录所有API访问

## 扩展部署

### 使用 PostgreSQL

修改 `backend/.env`:

```env
DATABASE_URL=postgresql://user:password@localhost/intelligence_db
```

安装PostgreSQL驱动:

```bash
pip install psycopg2-binary
```

### 添加 Redis 缓存

```bash
pip install redis
```

配置缓存策略

### Kubernetes 部署

参考 `k8s/` 目录中的配置文件

## 更新和维护

### 更新应用

```bash
# 拉取最新代码
git pull

# 更新后端
cd backend
pip install -r requirements.txt
alembic upgrade head

# 更新前端
cd ../frontend
npm install
npm run build

# 重启服务
systemctl restart ai-intelligence
```
