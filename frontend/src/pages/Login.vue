<template>
  <div class="auth-page">
    <section class="page-hero auth-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Login</span></div>
        <span class="tag">// Access Yantra tools</span>
        <h1 class="page-hero-title">Member Login</h1>
        <p class="page-hero-sub">Sign in with your Yantra account to access your dashboard and member-only tools.</p>
      </div>
    </section>

    <section class="section">
      <div class="container auth-card">
        <form class="auth-form" @submit.prevent="handleSubmit">
          <label>Email</label>
          <input type="email" v-model="email" required placeholder="name@domain.com" />

          <label>Password</label>
          <input type="password" v-model="password" required placeholder="Enter your password" />

          <button type="submit" class="btn btn-primary" :disabled="loading">
            {{ loading ? 'Signing in…' : 'Login' }}
          </button>

          <p v-if="errorMessage" class="auth-error">{{ errorMessage }}</p>
        </form>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, watchEffect, onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'

const userStore = useUserStore()
const router = useRouter()
const email = ref('')
const password = ref('')
const errorMessage = ref('')

const loading = ref(false)

async function handleSubmit() {
  errorMessage.value = ''
  loading.value = true
  try {
    await userStore.login(email.value, password.value)
    if (userStore.isAuthenticated) {
      router.push('/dashboard')
    } else {
      errorMessage.value = userStore.error || 'Login failed. Please try again.'
    }
  } catch (err) {
    errorMessage.value = err.response?.data?.error || err.message || userStore.error || 'Unable to login.'
    console.error('Login error', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  if (userStore.isAuthenticated) {
    router.replace('/dashboard')
  }
})

watchEffect(() => {
  if (userStore.error) {
    errorMessage.value = userStore.error
  }
})
</script>

<style scoped>
.auth-hero {
  padding-top: 110px;
}
.auth-card {
  max-width: 520px;
  margin: 0 auto;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 40px;
}
.auth-form {
  display: grid;
  gap: 20px;
}
.auth-form label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-muted);
}
.auth-form input {
  width: 100%;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--text-primary);
  border-radius: 12px;
  padding: 14px 16px;
}
.auth-error {
  color: #ff7a7a;
  font-size: 0.95rem;
  margin-top: 6px;
}
</style>
