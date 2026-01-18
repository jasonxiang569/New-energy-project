import json
import re
import time
from typing import Dict, Any, List
from anthropic import Anthropic
from ..core.config import settings


class AIAnalysisService:
    """AI情报分析服务"""

    def __init__(self):
        self.anthropic_client = None
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    async def analyze_intelligence(self, content: str, model: str = None) -> Dict[str, Any]:
        """
        对情报内容进行AI智能分析

        Args:
            content: 情报内容
            model: 使用的模型，默认使用配置中的模型

        Returns:
            分析结果字典
        """
        if not self.anthropic_client:
            raise ValueError("ANTHROPIC_API_KEY not configured")

        start_time = time.time()
        model = model or settings.DEFAULT_AI_MODEL

        # 构建分析提示词
        prompt = self._build_analysis_prompt(content)

        # 调用Claude API
        try:
            response = self.anthropic_client.messages.create(
                model=model,
                max_tokens=4096,
                temperature=0.3,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            analysis_text = response.content[0].text
            duration = int(time.time() - start_time)

            # 解析分析结果
            result = self._parse_analysis_result(analysis_text)
            result["analysis_duration"] = duration
            result["model_used"] = model
            result["full_analysis"] = analysis_text

            return result

        except Exception as e:
            raise Exception(f"AI分析失败: {str(e)}")

    def _build_analysis_prompt(self, content: str) -> str:
        """构建分析提示词"""
        return f"""请对以下情报内容进行全面的智能分析，并按照指定格式返回结果：

情报内容：
{content}

请提供以下分析：

1. **摘要** (Summary): 用1-2句话总结核心内容

2. **情感分析** (Sentiment):
   - 情感倾向: positive（正面）/ negative（负面）/ neutral（中性）
   - 情感得分: -100到100之间的整数（-100最负面，0中性，100最正面）

3. **实体识别** (Entities): 识别文本中的关键实体
   - 人物 (PERSON)
   - 组织 (ORGANIZATION)
   - 地点 (LOCATION)
   - 日期 (DATE)
   - 其他重要实体

4. **关键词** (Keywords): 提取5-10个最重要的关键词

5. **主题** (Topics): 识别3-5个主要主题或话题

6. **风险评估** (Risk Level):
   - low（低风险）
   - medium（中风险）
   - high（高风险）
   - critical（严重风险）

7. **洞察分析** (Insights): 提供3-5点深度洞察，包括：
   - 潜在影响
   - 趋势分析
   - 建议行动
   - 相关性分析

请严格按照以下JSON格式返回（只返回JSON，不要其他内容）：

{{
  "summary": "摘要内容",
  "sentiment": "positive|negative|neutral",
  "sentiment_score": 0,
  "entities": [
    {{"type": "PERSON", "text": "实体名称", "context": "上下文"}},
    {{"type": "ORGANIZATION", "text": "实体名称", "context": "上下文"}}
  ],
  "keywords": ["关键词1", "关键词2", "关键词3"],
  "topics": ["主题1", "主题2", "主题3"],
  "risk_level": "low|medium|high|critical",
  "insights": "详细的洞察分析，包含潜在影响、趋势、建议等"
}}
"""

    def _parse_analysis_result(self, analysis_text: str) -> Dict[str, Any]:
        """解析AI分析结果"""
        try:
            # 尝试提取JSON
            json_match = re.search(r'\{.*\}', analysis_text, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
            else:
                result = json.loads(analysis_text)

            # 验证必需字段
            required_fields = ["summary", "sentiment", "sentiment_score", "keywords", "topics", "risk_level"]
            for field in required_fields:
                if field not in result:
                    result[field] = self._get_default_value(field)

            # 确保entities是列表
            if "entities" not in result or not isinstance(result["entities"], list):
                result["entities"] = []

            # 确保insights存在
            if "insights" not in result:
                result["insights"] = result.get("summary", "")

            return result

        except json.JSONDecodeError:
            # 如果JSON解析失败，返回基础分析
            return self._create_fallback_analysis(analysis_text)

    def _get_default_value(self, field: str) -> Any:
        """获取字段默认值"""
        defaults = {
            "summary": "分析中...",
            "sentiment": "neutral",
            "sentiment_score": 0,
            "keywords": [],
            "topics": [],
            "entities": [],
            "risk_level": "low",
            "insights": ""
        }
        return defaults.get(field)

    def _create_fallback_analysis(self, text: str) -> Dict[str, Any]:
        """创建后备分析结果"""
        return {
            "summary": text[:200] + "..." if len(text) > 200 else text,
            "sentiment": "neutral",
            "sentiment_score": 0,
            "entities": [],
            "keywords": self._extract_simple_keywords(text),
            "topics": ["General"],
            "risk_level": "low",
            "insights": text
        }

    def _extract_simple_keywords(self, text: str, max_keywords: int = 5) -> List[str]:
        """简单的关键词提取（后备方案）"""
        # 简单的分词和过滤
        words = re.findall(r'\w+', text.lower())
        # 过滤常见词和短词
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        keywords = [w for w in words if len(w) > 3 and w not in stop_words]
        # 返回词频最高的关键词
        from collections import Counter
        return [word for word, _ in Counter(keywords).most_common(max_keywords)]


# 创建全局服务实例
ai_service = AIAnalysisService()
