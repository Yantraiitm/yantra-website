<template>
  <div>
    <section class="page-hero dashboard-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Dashboard</span></div>
        <span class="tag">// Logged in</span>
        <h1 class="page-hero-title">Welcome back, {{ user?.name }}</h1>
        <p class="page-hero-sub">Access your member dashboard, view protected sections, and continue building with Yantra.</p>
      </div>
    </section>

    <section class="section">
      <div class="container dashboard-grid">
        <article class="dashboard-card">
          <h3>Member profile</h3>
          <p>Email: {{ user?.email }}</p>
          <p>Roles: {{ user?.roles?.join(', ') || 'Member' }}</p>
        </article>

        <article class="dashboard-card">
          <h3>Quick links</h3>
          <ul>
            <li><RouterLink to="/projects">Projects</RouterLink></li>
            <li><RouterLink to="/events">Events</RouterLink></li>
            <li><RouterLink to="/team">Team</RouterLink></li>
          </ul>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'

const userStore = useUserStore()
const router = useRouter()

onMounted(async () => {
  if (!userStore.isAuthenticated) {
    await userStore.fetchCurrentUser()
  }
  if (!userStore.isAuthenticated) {
    router.replace('/login')
  }
})

const user = userStore.user
</script>

<style scoped>
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
.dashboard-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 28px;
}
.dashboard-card h3 {
  margin-bottom: 14px;
}
.dashboard-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 10px;
}
.dashboard-card a {
  color: var(--accent-cyan);
}
</style>
