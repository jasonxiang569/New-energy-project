import { useEffect, useState } from 'react'
import { Card, Row, Col, Statistic, Spin } from 'antd'
import {
  FileTextOutlined,
  CheckCircleOutlined,
  ClockCircleOutlined,
  WarningOutlined,
} from '@ant-design/icons'
import { statsApi } from '../services/api'
import type { Stats } from '../types'

const Dashboard = () => {
  const [stats, setStats] = useState<Stats | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadStats()
  }, [])

  const loadStats = async () => {
    try {
      const response = await statsApi.get()
      setStats(response.data)
    } catch (error) {
      console.error('Failed to load stats:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <Spin size="large" style={{ display: 'block', margin: '100px auto' }} />
  }

  return (
    <div>
      <Row gutter={[16, 16]}>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="总情报数"
              value={stats?.total_intelligences || 0}
              prefix={<FileTextOutlined />}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="已完成"
              value={stats?.completed || 0}
              prefix={<CheckCircleOutlined />}
              valueStyle={{ color: '#3f8600' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="待分析"
              value={stats?.pending || 0}
              prefix={<ClockCircleOutlined />}
              valueStyle={{ color: '#1890ff' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="分析失败"
              value={stats?.failed || 0}
              prefix={<WarningOutlined />}
              valueStyle={{ color: '#cf1322' }}
            />
          </Card>
        </Col>
      </Row>

      <Row gutter={[16, 16]} style={{ marginTop: 16 }}>
        <Col xs={24} lg={12}>
          <Card title="按类型统计" bordered={false}>
            {stats?.by_type && Object.entries(stats.by_type).map(([type, count]) => (
              <div key={type} style={{ marginBottom: 8 }}>
                <span style={{ fontWeight: 500 }}>{type}:</span> {count}
              </div>
            ))}
          </Card>
        </Col>
        <Col xs={24} lg={12}>
          <Card title="情感分析统计" bordered={false}>
            {stats?.by_sentiment && Object.entries(stats.by_sentiment).map(([sentiment, count]) => (
              <div key={sentiment} style={{ marginBottom: 8 }}>
                <span style={{ fontWeight: 500 }}>{sentiment}:</span> {count}
              </div>
            ))}
          </Card>
        </Col>
      </Row>

      <Row gutter={[16, 16]} style={{ marginTop: 16 }}>
        <Col xs={24}>
          <Card title="风险等级统计" bordered={false}>
            {stats?.by_risk_level && Object.entries(stats.by_risk_level).map(([risk, count]) => (
              <div key={risk} style={{ marginBottom: 8 }}>
                <span style={{ fontWeight: 500 }}>{risk}:</span> {count}
              </div>
            ))}
          </Card>
        </Col>
      </Row>
    </div>
  )
}

export default Dashboard
