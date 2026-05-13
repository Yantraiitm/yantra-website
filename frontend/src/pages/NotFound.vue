<template>
  <div style="min-height: 80vh; display: flex; align-items: center; justify-content: center;">
    <div class="container" style="text-align: center;">
      <div style="font-size: 5rem; margin-bottom: 24px;">404</div>
      <h1 class="section-title" style="margin-bottom: 16px;">Page Not Found</h1>
      <p style="font-size: 1rem; color: var(--text-dim); margin-bottom: 32px; max-width: 500px; margin-left: auto; margin-right: auto;">
        Oops! The page you're looking for doesn't exist. But don't worry, there's plenty of cool stuff to explore on Yantra's website.
      </p>
      <RouterLink to="/" class="btn btn-amber">Go Home</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
