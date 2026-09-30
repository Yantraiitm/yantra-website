import axios from 'axios'
import { beginApiRequest, endApiRequest } from './networkState'

const API_URL = import.meta.env.VITE_API_BASE_URL || import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

export const apiClient = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    beginApiRequest(config)
    const token = localStorage.getItem('auth_token')
    const isAuthEndpoint = config.url?.includes('/auth/login') || config.url?.includes('/auth/register')

    if (token && !isAuthEndpoint) {
      config.headers.Authorization = token
    }
    return config
  },
  (error) => {
    endApiRequest(error.config)
    return Promise.reject(error)
  }
)

// Response interceptor
apiClient.interceptors.response.use(
  (response) => {
    endApiRequest(response.config)
    return response
  },
  (error) => {
    endApiRequest(error.config)
    const isLoginRequest = error.config?.url?.includes('/auth/login')
    if (error.response?.status === 401 && !isLoginRequest) {
      localStorage.removeItem('auth_token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default apiClient
