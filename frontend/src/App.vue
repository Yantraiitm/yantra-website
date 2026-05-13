<template>
  <div id="app" class="app-container">
    <!-- Preloader -->
    <Preloader v-if="showPreloader" />
    
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Preloader from './components/Preloader.vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

const router = useRouter()
const showPreloader = ref(true)

onMounted(() => {
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
