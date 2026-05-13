import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import apiClient from '../services/api'

export const useBlogStore = defineStore('blog', () => {
  const posts = ref([])
  const currentPost = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const publishedPosts = computed(() => posts.value.filter(p => p.published))

  async function fetchPosts() {
    loading.value = true
    try {
      const { data } = await apiClient.get('/blog')
      posts.value = data
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  async function fetchPost(id) {
    loading.value = true
    try {
      const { data } = await apiClient.get(`/blog/${id}`)
      currentPost.value = data
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  async function createPost(postData) {
    try {
      const { data } = await apiClient.post('/blog', postData)
      posts.value.push(data)
      return data
    } catch (err) {
      error.value = err.message
    }
  }

  async function updatePost(id, postData) {
    try {
      const { data } = await apiClient.put(`/blog/${id}`, postData)
      const index = posts.value.findIndex(p => p.id === id)
      if (index > -1) posts.value[index] = data
      return data
    } catch (err) {
      error.value = err.message
    }
  }

  async function deletePost(id) {
    try {
      await apiClient.delete(`/blog/${id}`)
      posts.value = posts.value.filter(p => p.id !== id)
    } catch (err) {
      error.value = err.message
    }
  }

  return {
    posts,
    currentPost,
    loading,
    error,
    publishedPosts,
    fetchPosts,
    fetchPost,
    createPost,
    updatePost,
    deletePost
  }
})
