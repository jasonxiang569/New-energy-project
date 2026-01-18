import { useState } from 'react'
import { Layout, Menu, Typography } from 'antd'
import {
  DashboardOutlined,
  FileTextOutlined,
  BarChartOutlined,
  ThunderboltOutlined,
} from '@ant-design/icons'
import Dashboard from './pages/Dashboard'
import IntelligenceList from './pages/IntelligenceList'
import QuickAnalysis from './pages/QuickAnalysis'
import './styles/App.css'

const { Header, Sider, Content } = Layout
const { Title } = Typography

type PageType = 'dashboard' | 'intelligence' | 'quick' | 'stats'

function App() {
  const [currentPage, setCurrentPage] = useState<PageType>('dashboard')

  const renderContent = () => {
    switch (currentPage) {
      case 'dashboard':
        return <Dashboard />
      case 'intelligence':
        return <IntelligenceList />
      case 'quick':
        return <QuickAnalysis />
      default:
        return <Dashboard />
    }
  }

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider width={240} theme="dark">
        <div style={{ padding: '20px', textAlign: 'center' }}>
          <Title level={4} style={{ color: 'white', margin: 0 }}>
            AI情报系统
          </Title>
        </div>
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[currentPage]}
          onClick={({ key }) => setCurrentPage(key as PageType)}
          items={[
            {
              key: 'dashboard',
              icon: <DashboardOutlined />,
              label: '仪表盘',
            },
            {
              key: 'intelligence',
              icon: <FileTextOutlined />,
              label: '情报管理',
            },
            {
              key: 'quick',
              icon: <ThunderboltOutlined />,
              label: '快速分析',
            },
            {
              key: 'stats',
              icon: <BarChartOutlined />,
              label: '统计分析',
            },
          ]}
        />
      </Sider>
      <Layout>
        <Header style={{ background: '#fff', padding: '0 24px' }}>
          <Title level={3} style={{ margin: '14px 0' }}>
            {currentPage === 'dashboard' && '仪表盘'}
            {currentPage === 'intelligence' && '情报管理'}
            {currentPage === 'quick' && '快速分析'}
            {currentPage === 'stats' && '统计分析'}
          </Title>
        </Header>
        <Content style={{ margin: '24px', background: '#fff', padding: '24px', minHeight: 280 }}>
          {renderContent()}
        </Content>
      </Layout>
    </Layout>
  )
}

export default App
