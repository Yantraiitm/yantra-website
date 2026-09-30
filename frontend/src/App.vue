<template>
  <div id="app" class="app-container">
    <!-- Preloader -->
    <Preloader v-if="showPreloader" />
    <RoboticsLoader v-if="showApiLoader && !showPreloader" compact floating label="Communicating with Yantra" />
    
    <!-- Navbar -->
    <Navbar />
    
    <!-- Main Content -->
    <main class="main-content">
      <RouterView />
    </main>
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from './stores/user'
import Preloader from './components/Preloader.vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import RoboticsLoader from './components/RoboticsLoader.vue'
import { activeApiRequests } from './services/networkState'

const router = useRouter()
const showPreloader = ref(true)
const userStore = useUserStore()
const showApiLoader = ref(false)
let apiLoaderTimer

watch(activeApiRequests, (count) => {
  clearTimeout(apiLoaderTimer)
  if (count > 0) apiLoaderTimer = setTimeout(() => { showApiLoader.value = true }, 180)
  else showApiLoader.value = false
})

onMounted(() => {
  if (localStorage.getItem('auth_token')) {
    userStore.fetchCurrentUser().catch(() => {})
  }

  // Show preloader for initial load only
  setTimeout(() => {
    showPreloader.value = false
    document.body.style.overflow = ''
  }, 1950)
})
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}
</style>
