import axios from 'axios'
import type {
  Intelligence,
  IntelligenceCreate,
  Analysis,
  QuickAnalysisRequest,
  QuickAnalysisResponse,
  Stats,
} from '../types'

const api = axios.create({
  baseURL: '/api',
  timeout: 60000, // AI分析可能需要较长时间
})

// Intelligence API
export const intelligenceApi = {
  create: (data: IntelligenceCreate) =>
    api.post<Intelligence>('/intelligence/', data),

  getById: (id: number) =>
    api.get<Intelligence>(`/intelligence/${id}`),

  list: (params?: { skip?: number; limit?: number; status?: string; type?: string }) =>
    api.get<{ total: number; items: Intelligence[] }>('/intelligence/', { params }),

  update: (id: number, data: Partial<IntelligenceCreate>) =>
    api.put<Intelligence>(`/intelligence/${id}`, data),

  delete: (id: number) =>
    api.delete(`/intelligence/${id}`),

  analyze: (id: number, model?: string) =>
    api.post<Analysis>(`/intelligence/${id}/analyze`, model ? { model } : {}),

  getAnalyses: (id: number) =>
    api.get<Analysis[]>(`/intelligence/${id}/analyses`),

  quickAnalyze: (data: QuickAnalysisRequest) =>
    api.post<QuickAnalysisResponse>('/intelligence/quick-analyze', data),
}

// Stats API
export const statsApi = {
  get: () => api.get<Stats>('/stats/'),
}

export default api
