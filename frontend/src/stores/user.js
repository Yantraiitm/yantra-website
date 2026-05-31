import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authService } from '../services/auth'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!user.value)
  const isAdmin = computed(() => user.value?.roles?.includes('admin'))

  async function fetchCurrentUser() {
    loading.value = true
    try {
      const currentUser = await authService.getCurrentUser()
      user.value = currentUser
      error.value = null
    } catch (err) {
      error.value = err.response?.data?.error || err.message
      user.value = null
    } finally {
      loading.value = false
    }
  }

  async function login(email, password) {
    loading.value = true
    error.value = null
    try {
      const data = await authService.login(email, password)
      localStorage.setItem('auth_token', data.token)
      user.value = data.user
    } catch (err) {
      error.value = err.response?.data?.error || err.message
      user.value = null
      throw err
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    loading.value = true
    try {
      await authService.logout()
      user.value = null
      localStorage.removeItem('auth_token')
      error.value = null
    } catch (err) {
      error.value = err.response?.data?.error || err.message
    } finally {
      loading.value = false
    }
  }

  return {
    user,
    loading,
    error,
    isAuthenticated,
    isAdmin,
    fetchCurrentUser,
    login,
    logout
  }
})
