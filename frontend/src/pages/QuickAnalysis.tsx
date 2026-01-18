import { useState } from 'react'
import { Card, Input, Button, Space, Typography, Tag, Divider, Spin, message } from 'antd'
import { ThunderboltOutlined } from '@ant-design/icons'
import { intelligenceApi } from '../services/api'
import type { QuickAnalysisResponse } from '../types'

const { TextArea } = Input
const { Title, Paragraph, Text } = Typography

const QuickAnalysis = () => {
  const [content, setContent] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<QuickAnalysisResponse | null>(null)

  const handleAnalyze = async () => {
    if (!content.trim()) {
      message.warning('请输入要分析的内容')
      return
    }

    setLoading(true)
    try {
      const response = await intelligenceApi.quickAnalyze({ content })
      setResult(response.data)
      message.success('分析完成')
    } catch (error: any) {
      message.error(error.response?.data?.detail || '分析失败，请检查API配置')
    } finally {
      setLoading(false)
    }
  }

  const getRiskColor = (risk: string) => {
    const colors: Record<string, string> = {
      low: 'green',
      medium: 'orange',
      high: 'red',
      critical: 'purple',
    }
    return colors[risk] || 'default'
  }

  const getSentimentColor = (sentiment: string) => {
    const colors: Record<string, string> = {
      positive: 'green',
      negative: 'red',
      neutral: 'blue',
    }
    return colors[sentiment.toLowerCase()] || 'default'
  }

  return (
    <div>
      <Card title="输入要分析的内容">
        <TextArea
          rows={8}
          placeholder="请输入要分析的文本内容..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
          style={{ marginBottom: 16 }}
        />
        <Button
          type="primary"
          icon={<ThunderboltOutlined />}
          onClick={handleAnalyze}
          loading={loading}
          size="large"
        >
          快速分析
        </Button>
      </Card>

      {loading && (
        <Card style={{ marginTop: 16, textAlign: 'center' }}>
          <Spin size="large" />
          <Paragraph style={{ marginTop: 16 }}>
            AI正在分析中，请稍候...
          </Paragraph>
        </Card>
      )}

      {result && !loading && (
        <Card title="分析结果" style={{ marginTop: 16 }}>
          <Space direction="vertical" size="large" style={{ width: '100%' }}>
            {/* 摘要 */}
            <div>
              <Title level={5}>摘要</Title>
              <Paragraph>{result.summary}</Paragraph>
            </div>

            <Divider />

            {/* 情感分析 */}
            <div>
              <Title level={5}>情感分析</Title>
              <Space>
                <Tag color={getSentimentColor(result.sentiment)} style={{ fontSize: 14 }}>
                  {result.sentiment}
                </Tag>
                <Text>得分: {result.sentiment_score}</Text>
              </Space>
            </div>

            <Divider />

            {/* 风险等级 */}
            <div>
              <Title level={5}>风险等级</Title>
              <Tag color={getRiskColor(result.risk_level)} style={{ fontSize: 14 }}>
                {result.risk_level}
              </Tag>
            </div>

            <Divider />

            {/* 关键词 */}
            <div>
              <Title level={5}>关键词</Title>
              <Space wrap>
                {result.keywords.map((keyword, index) => (
                  <Tag key={index} color="blue">{keyword}</Tag>
                ))}
              </Space>
            </div>

            <Divider />

            {/* 主题 */}
            <div>
              <Title level={5}>主题</Title>
              <Space wrap>
                {result.topics.map((topic, index) => (
                  <Tag key={index} color="purple">{topic}</Tag>
                ))}
              </Space>
            </div>

            <Divider />

            {/* 实体识别 */}
            {result.entities.length > 0 && (
              <>
                <div>
                  <Title level={5}>实体识别</Title>
                  <Space direction="vertical" style={{ width: '100%' }}>
                    {result.entities.map((entity, index) => (
                      <div key={index}>
                        <Tag color="cyan">{entity.type}</Tag>
                        <Text strong>{entity.text}</Text>
                        {entity.context && <Text type="secondary"> - {entity.context}</Text>}
                      </div>
                    ))}
                  </Space>
                </div>
                <Divider />
              </>
            )}

            {/* 洞察分析 */}
            <div>
              <Title level={5}>洞察分析</Title>
              <Paragraph style={{ whiteSpace: 'pre-wrap' }}>
                {result.insights}
              </Paragraph>
            </div>

            <Divider />

            {/* 完整分析 */}
            <div>
              <Title level={5}>完整分析报告</Title>
              <Paragraph style={{ whiteSpace: 'pre-wrap', background: '#f5f5f5', padding: 16 }}>
                {result.full_analysis}
              </Paragraph>
            </div>
          </Space>
        </Card>
      )}
    </div>
  )
}

export default QuickAnalysis
