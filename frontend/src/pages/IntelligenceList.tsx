import { useEffect, useState } from 'react'
import {
  Table,
  Button,
  Modal,
  Form,
  Input,
  Select,
  Tag,
  Space,
  message,
  Spin,
  Typography,
} from 'antd'
import { PlusOutlined, ThunderboltOutlined, EyeOutlined } from '@ant-design/icons'
import { intelligenceApi } from '../services/api'
import type { Intelligence, IntelligenceCreate, Analysis } from '../types'
import { IntelligenceStatus, IntelligenceType } from '../types'

const { TextArea } = Input
const { Paragraph, Text } = Typography

const IntelligenceList = () => {
  const [data, setData] = useState<Intelligence[]>([])
  const [loading, setLoading] = useState(false)
  const [total, setTotal] = useState(0)
  const [createModalVisible, setCreateModalVisible] = useState(false)
  const [detailModalVisible, setDetailModalVisible] = useState(false)
  const [selectedIntelligence, setSelectedIntelligence] = useState<Intelligence | null>(null)
  const [analysis, setAnalysis] = useState<Analysis | null>(null)
  const [analyzing, setAnalyzing] = useState(false)
  const [form] = Form.useForm()

  useEffect(() => {
    loadData()
  }, [])

  const loadData = async () => {
    setLoading(true)
    try {
      const response = await intelligenceApi.list({ limit: 100 })
      setData(response.data.items)
      setTotal(response.data.total)
    } catch (error) {
      message.error('加载数据失败')
    } finally {
      setLoading(false)
    }
  }

  const handleCreate = async (values: IntelligenceCreate) => {
    try {
      await intelligenceApi.create(values)
      message.success('创建成功')
      setCreateModalVisible(false)
      form.resetFields()
      loadData()
    } catch (error) {
      message.error('创建失败')
    }
  }

  const handleAnalyze = async (id: number) => {
    setAnalyzing(true)
    try {
      const response = await intelligenceApi.analyze(id)
      message.success('分析完成')
      setAnalysis(response.data)
      loadData()
    } catch (error: any) {
      message.error(error.response?.data?.detail || '分析失败')
    } finally {
      setAnalyzing(false)
    }
  }

  const handleViewDetail = async (record: Intelligence) => {
    setSelectedIntelligence(record)
    setDetailModalVisible(true)
    setAnalysis(null)

    // 加载分析结果
    try {
      const response = await intelligenceApi.getAnalyses(record.id)
      if (response.data.length > 0) {
        setAnalysis(response.data[0])
      }
    } catch (error) {
      console.error('Failed to load analysis:', error)
    }
  }

  const getStatusColor = (status: IntelligenceStatus) => {
    const colors = {
      [IntelligenceStatus.PENDING]: 'blue',
      [IntelligenceStatus.ANALYZING]: 'orange',
      [IntelligenceStatus.COMPLETED]: 'green',
      [IntelligenceStatus.FAILED]: 'red',
    }
    return colors[status]
  }

  const getRiskColor = (risk?: string) => {
    const colors: Record<string, string> = {
      low: 'green',
      medium: 'orange',
      high: 'red',
      critical: 'purple',
    }
    return risk ? colors[risk] : 'default'
  }

  const columns = [
    {
      title: 'ID',
      dataIndex: 'id',
      key: 'id',
      width: 60,
    },
    {
      title: '标题',
      dataIndex: 'title',
      key: 'title',
      ellipsis: true,
    },
    {
      title: '类型',
      dataIndex: 'type',
      key: 'type',
      width: 120,
    },
    {
      title: '状态',
      dataIndex: 'status',
      key: 'status',
      width: 100,
      render: (status: IntelligenceStatus) => (
        <Tag color={getStatusColor(status)}>{status}</Tag>
      ),
    },
    {
      title: '创建时间',
      dataIndex: 'created_at',
      key: 'created_at',
      width: 180,
      render: (date: string) => new Date(date).toLocaleString('zh-CN'),
    },
    {
      title: '操作',
      key: 'action',
      width: 200,
      render: (_: any, record: Intelligence) => (
        <Space>
          <Button
            size="small"
            icon={<EyeOutlined />}
            onClick={() => handleViewDetail(record)}
          >
            详情
          </Button>
          <Button
            size="small"
            type="primary"
            icon={<ThunderboltOutlined />}
            onClick={() => handleAnalyze(record.id)}
            disabled={record.status === IntelligenceStatus.ANALYZING}
            loading={analyzing}
          >
            分析
          </Button>
        </Space>
      ),
    },
  ]

  return (
    <div>
      <div style={{ marginBottom: 16 }}>
        <Button
          type="primary"
          icon={<PlusOutlined />}
          onClick={() => setCreateModalVisible(true)}
        >
          新建情报
        </Button>
      </div>

      <Table
        columns={columns}
        dataSource={data}
        rowKey="id"
        loading={loading}
        pagination={{ total, pageSize: 100 }}
      />

      {/* 创建情报Modal */}
      <Modal
        title="新建情报"
        open={createModalVisible}
        onCancel={() => {
          setCreateModalVisible(false)
          form.resetFields()
        }}
        onOk={() => form.submit()}
        width={600}
      >
        <Form form={form} layout="vertical" onFinish={handleCreate}>
          <Form.Item
            name="title"
            label="标题"
            rules={[{ required: true, message: '请输入标题' }]}
          >
            <Input placeholder="请输入情报标题" />
          </Form.Item>
          <Form.Item
            name="content"
            label="内容"
            rules={[{ required: true, message: '请输入内容' }]}
          >
            <TextArea rows={6} placeholder="请输入情报内容" />
          </Form.Item>
          <Form.Item name="source" label="来源">
            <Input placeholder="请输入情报来源" />
          </Form.Item>
          <Form.Item name="type" label="类型" initialValue={IntelligenceType.TEXT}>
            <Select>
              <Select.Option value={IntelligenceType.TEXT}>文本</Select.Option>
              <Select.Option value={IntelligenceType.NEWS}>新闻</Select.Option>
              <Select.Option value={IntelligenceType.REPORT}>报告</Select.Option>
              <Select.Option value={IntelligenceType.SOCIAL_MEDIA}>社交媒体</Select.Option>
              <Select.Option value={IntelligenceType.OTHER}>其他</Select.Option>
            </Select>
          </Form.Item>
        </Form>
      </Modal>

      {/* 详情Modal */}
      <Modal
        title="情报详情"
        open={detailModalVisible}
        onCancel={() => setDetailModalVisible(false)}
        footer={null}
        width={800}
      >
        {selectedIntelligence && (
          <div>
            <Paragraph>
              <Text strong>标题：</Text>
              {selectedIntelligence.title}
            </Paragraph>
            <Paragraph>
              <Text strong>内容：</Text>
              <br />
              {selectedIntelligence.content}
            </Paragraph>
            <Paragraph>
              <Text strong>来源：</Text>
              {selectedIntelligence.source || '未知'}
            </Paragraph>
            <Paragraph>
              <Text strong>类型：</Text>
              {selectedIntelligence.type}
            </Paragraph>
            <Paragraph>
              <Text strong>状态：</Text>
              <Tag color={getStatusColor(selectedIntelligence.status)}>
                {selectedIntelligence.status}
              </Tag>
            </Paragraph>

            {analysis && (
              <>
                <Typography.Title level={5} style={{ marginTop: 24 }}>
                  AI分析结果
                </Typography.Title>
                <Paragraph>
                  <Text strong>摘要：</Text>
                  <br />
                  {analysis.summary}
                </Paragraph>
                <Paragraph>
                  <Text strong>情感分析：</Text>
                  {analysis.sentiment} (得分: {analysis.sentiment_score})
                </Paragraph>
                <Paragraph>
                  <Text strong>风险等级：</Text>
                  <Tag color={getRiskColor(analysis.risk_level)}>
                    {analysis.risk_level}
                  </Tag>
                </Paragraph>
                <Paragraph>
                  <Text strong>关键词：</Text>
                  <br />
                  {analysis.keywords.map(kw => (
                    <Tag key={kw}>{kw}</Tag>
                  ))}
                </Paragraph>
                <Paragraph>
                  <Text strong>主题：</Text>
                  <br />
                  {analysis.topics.map(topic => (
                    <Tag key={topic} color="blue">{topic}</Tag>
                  ))}
                </Paragraph>
                <Paragraph>
                  <Text strong>洞察分析：</Text>
                  <br />
                  {analysis.insights}
                </Paragraph>
              </>
            )}
          </div>
        )}
      </Modal>
    </div>
  )
}

export default IntelligenceList
