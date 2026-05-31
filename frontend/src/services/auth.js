import apiClient from './api'

export const authService = {
  async login(email, password) {
    const response = await apiClient.post('/auth/login', { email, password })
    return response.data
  },

  async getCurrentUser() {
    const response = await apiClient.get('/auth/me')
    return response.data
  },

  async logout() {
    localStorage.removeItem('auth_token')
    return true
  }
}
