<template>
  <div id="preloader" :class="{ done: isDone }">
    <div class="pre-center">
      <div class="pre-ring"></div>
      <span class="pre-glyph">⚙</span>
    </div>
    <div class="pre-bar-track">
      <div class="pre-bar-fill"></div>
    </div>
    <div class="pre-text">Loading Yantra...</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isDone = ref(false)

defineProps({
  show: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['done'])

// Simulate loading completion
setTimeout(() => {
  isDone.value = true
  emit('done')
}, 1950)
</script>

<style scoped>
#preloader {
  position: fixed;
  inset: 0;
  background: #0E0E0E;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  transition: opacity 0.55s ease, visibility 0.55s ease;
}

#preloader.done {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.pre-center {
  position: relative;
  width: 68px;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pre-ring {
  width: 68px;
  height: 68px;
  border: 2px solid var(--muted);
  border-top-color: var(--amber);
  border-right-color: var(--rust);
  border-radius: 50%;
  position: absolute;
  animation: preSpinA 1s linear infinite;
}

.pre-glyph {
  font-size: 1.7rem;
  animation: preSpinA 1s linear infinite reverse;
}

.pre-bar-track {
  width: 180px;
  height: 2px;
  background: var(--muted);
  border-radius: 2px;
  overflow: hidden;
}

.pre-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--amber), var(--rust));
  border-radius: 2px;
  animation: preLoad 1.85s ease forwards;
}

.pre-text {
  font-family: 'DM Mono', monospace;
  font-size: 0.62rem;
  color: var(--slate);
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

@keyframes preSpinA {
  to {
    transform: rotate(360deg);
  }
}

@keyframes preLoad {
  0% { width: 0; }
  60% { width: 70%; }
  100% { width: 100%; }
}
</style>
