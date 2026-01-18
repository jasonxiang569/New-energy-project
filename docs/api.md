# API 文档

## 基础信息

- **Base URL**: `http://localhost:8000/api`
- **Content-Type**: `application/json`
- **响应格式**: JSON

## 情报管理 API

### 1. 创建情报

创建新的情报数据。

**请求**

```http
POST /api/intelligence/
Content-Type: application/json

{
  "title": "情报标题",
  "content": "情报内容文本...",
  "source": "信息来源",
  "type": "text",
  "tags": ["标签1", "标签2"],
  "metadata": {}
}
```

**字段说明**

- `title` (必需): 情报标题
- `content` (必需): 情报内容
- `source` (可选): 信息来源
- `type` (可选): 类型，可选值: `text`, `news`, `report`, `social_media`, `other`
- `tags` (可选): 标签数组
- `metadata` (可选): 额外元数据对象

**响应**

```json
{
  "id": 1,
  "title": "情报标题",
  "content": "情报内容文本...",
  "source": "信息来源",
  "type": "text",
  "status": "pending",
  "tags": ["标签1", "标签2"],
  "metadata": {},
  "created_at": "2024-01-17T10:00:00",
  "updated_at": null
}
```

### 2. 获取情报列表

获取所有情报数据，支持分页和筛选。

**请求**

```http
GET /api/intelligence/?skip=0&limit=100&status=pending&type=text
```

**查询参数**

- `skip` (可选): 跳过的记录数，默认0
- `limit` (可选): 返回的最大记录数，默认100
- `status` (可选): 按状态筛选: `pending`, `analyzing`, `completed`, `failed`
- `type` (可选): 按类型筛选

**响应**

```json
{
  "total": 50,
  "items": [
    {
      "id": 1,
      "title": "情报标题",
      "content": "情报内容...",
      "status": "completed",
      ...
    }
  ]
}
```

### 3. 获取单个情报

获取指定ID的情报详情。

**请求**

```http
GET /api/intelligence/{id}
```

**响应**

```json
{
  "id": 1,
  "title": "情报标题",
  "content": "情报内容...",
  "status": "completed",
  ...
}
```

### 4. 更新情报

更新指定ID的情报信息。

**请求**

```http
PUT /api/intelligence/{id}
Content-Type: application/json

{
  "title": "更新后的标题",
  "status": "completed"
}
```

**响应**

返回更新后的情报对象

### 5. 删除情报

删除指定ID的情报及其相关分析。

**请求**

```http
DELETE /api/intelligence/{id}
```

**响应**

- Status: 204 No Content

## AI 分析 API

### 6. 分析情报

对指定情报进行AI智能分析。

**请求**

```http
POST /api/intelligence/{id}/analyze
Content-Type: application/json

{
  "model": "claude-3-sonnet-20240229"
}
```

**字段说明**

- `model` (可选): 使用的AI模型，默认使用配置中的模型

**响应**

```json
{
  "id": 1,
  "intelligence_id": 1,
  "summary": "这是对情报内容的摘要...",
  "sentiment": "positive",
  "sentiment_score": 75,
  "entities": [
    {
      "type": "PERSON",
      "text": "张三",
      "context": "提到的人名"
    }
  ],
  "keywords": ["关键词1", "关键词2", "关键词3"],
  "topics": ["主题1", "主题2"],
  "risk_level": "low",
  "insights": "详细的洞察分析...",
  "full_analysis": "完整的分析报告...",
  "model_used": "claude-3-sonnet-20240229",
  "analysis_duration": 5,
  "created_at": "2024-01-17T10:05:00"
}
```

**字段说明**

- `summary`: 内容摘要
- `sentiment`: 情感倾向 (positive/negative/neutral)
- `sentiment_score`: 情感得分 (-100 到 100)
- `entities`: 识别的实体列表
- `keywords`: 关键词列表
- `topics`: 主题列表
- `risk_level`: 风险等级 (low/medium/high/critical)
- `insights`: AI洞察分析
- `full_analysis`: 完整分析文本
- `model_used`: 使用的AI模型
- `analysis_duration`: 分析耗时（秒）

### 7. 获取情报的分析结果

获取某个情报的所有分析历史。

**请求**

```http
GET /api/intelligence/{id}/analyses
```

**响应**

返回分析结果数组，按时间倒序排列

### 8. 快速分析

快速分析文本内容，不保存到数据库。

**请求**

```http
POST /api/intelligence/quick-analyze
Content-Type: application/json

{
  "content": "要分析的文本内容...",
  "model": "claude-3-sonnet-20240229"
}
```

**响应**

```json
{
  "summary": "内容摘要...",
  "sentiment": "neutral",
  "sentiment_score": 0,
  "entities": [],
  "keywords": ["关键词1", "关键词2"],
  "topics": ["主题1"],
  "risk_level": "low",
  "insights": "洞察分析...",
  "full_analysis": "完整分析..."
}
```

## 统计 API

### 9. 获取系统统计

获取系统的整体统计数据。

**请求**

```http
GET /api/stats/
```

**响应**

```json
{
  "total_intelligences": 100,
  "pending": 10,
  "analyzing": 5,
  "completed": 80,
  "failed": 5,
  "total_analyses": 85,
  "by_type": {
    "text": 50,
    "news": 30,
    "report": 20
  },
  "by_sentiment": {
    "positive": 40,
    "negative": 20,
    "neutral": 25
  },
  "by_risk_level": {
    "low": 50,
    "medium": 25,
    "high": 8,
    "critical": 2
  }
}
```

## 错误响应

所有API在发生错误时返回统一格式：

```json
{
  "detail": "错误描述信息"
}
```

**HTTP状态码**

- `200`: 成功
- `201`: 创建成功
- `204`: 删除成功（无内容）
- `400`: 请求参数错误
- `404`: 资源不存在
- `500`: 服务器内部错误

## 使用示例

### Python 示例

```python
import requests

# 创建情报
response = requests.post('http://localhost:8000/api/intelligence/', json={
    'title': '测试情报',
    'content': '这是测试内容...'
})
intelligence = response.json()

# 分析情报
analysis = requests.post(
    f'http://localhost:8000/api/intelligence/{intelligence["id"]}/analyze'
).json()

print(f"分析结果: {analysis['summary']}")
print(f"风险等级: {analysis['risk_level']}")
```

### JavaScript 示例

```javascript
// 创建情报
const response = await fetch('http://localhost:8000/api/intelligence/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    title: '测试情报',
    content: '这是测试内容...'
  })
})
const intelligence = await response.json()

// 快速分析
const analysis = await fetch('http://localhost:8000/api/intelligence/quick-analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    content: '要分析的文本...'
  })
})
const result = await analysis.json()

console.log('摘要:', result.summary)
console.log('情感:', result.sentiment)
```

### cURL 示例

```bash
# 创建情报
curl -X POST http://localhost:8000/api/intelligence/ \
  -H "Content-Type: application/json" \
  -d '{"title":"测试","content":"测试内容"}'

# 快速分析
curl -X POST http://localhost:8000/api/intelligence/quick-analyze \
  -H "Content-Type: application/json" \
  -d '{"content":"要分析的文本内容..."}'

# 获取统计
curl http://localhost:8000/api/stats/
```

## 交互式文档

启动后端服务后，可以访问自动生成的交互式API文档：

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

在这些页面中可以直接测试所有API端点。
