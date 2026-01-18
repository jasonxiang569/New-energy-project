export enum IntelligenceStatus {
  PENDING = 'pending',
  ANALYZING = 'analyzing',
  COMPLETED = 'completed',
  FAILED = 'failed',
}

export enum IntelligenceType {
  TEXT = 'text',
  NEWS = 'news',
  REPORT = 'report',
  SOCIAL_MEDIA = 'social_media',
  OTHER = 'other',
}

export interface Intelligence {
  id: number
  title: string
  content: string
  source?: string
  type: IntelligenceType
  status: IntelligenceStatus
  tags: string[]
  metadata: Record<string, any>
  created_at: string
  updated_at?: string
}

export interface Entity {
  type: string
  text: string
  context?: string
}

export interface Analysis {
  id: number
  intelligence_id: number
  summary?: string
  sentiment?: string
  sentiment_score?: number
  entities: Entity[]
  keywords: string[]
  topics: string[]
  risk_level?: string
  insights?: string
  full_analysis?: string
  model_used?: string
  analysis_duration?: number
  created_at: string
}

export interface IntelligenceCreate {
  title: string
  content: string
  source?: string
  type?: IntelligenceType
  tags?: string[]
  metadata?: Record<string, any>
}

export interface QuickAnalysisRequest {
  content: string
  model?: string
}

export interface QuickAnalysisResponse {
  summary: string
  sentiment: string
  sentiment_score: number
  entities: Entity[]
  keywords: string[]
  topics: string[]
  risk_level: string
  insights: string
  full_analysis: string
}

export interface Stats {
  total_intelligences: number
  pending: number
  analyzing: number
  completed: number
  failed: number
  total_analyses: number
  by_type: Record<string, number>
  by_sentiment: Record<string, number>
  by_risk_level: Record<string, number>
}
