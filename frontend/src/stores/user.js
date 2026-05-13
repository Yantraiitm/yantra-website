import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authService } from '../services/supabase'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!user.value)
  const isAdmin = computed(() => user.value?.role === 'admin')

  async function getCurrentUser() {
    loading.value = true
    try {
      const currentUser = await authService.getCurrentUser()
      user.value = currentUser
    } catch (err) {
      error.value = err.message
      user.value = null
    } finally {
      loading.value = false
    }
  }

  async function login(email, password) {
    loading.value = true
    try {
      const session = await authService.signIn(email, password)
      user.value = session.user
      localStorage.setItem('auth_token', session.session.access_token)
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    loading.value = true
    try {
      await authService.signOut()
      user.value = null
      localStorage.removeItem('auth_token')
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  async function signup(email, password) {
    loading.value = true
    try {
      const data = await authService.signUp(email, password)
      user.value = data.user
    } catch (err) {
      error.value = err.message
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
    getCurrentUser,
    login,
    logout,
    signup
  }
})
