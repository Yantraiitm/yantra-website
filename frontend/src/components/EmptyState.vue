<template>
  <div class="empty-state" role="status">
    <div class="empty-icon" aria-hidden="true">
      <svg viewBox="0 0 48 48" fill="none"><path d="M24 5v6m0 26v6M5 24h6m26 0h6M10.6 10.6l4.3 4.3m18.2 18.2 4.3 4.3m0-26.8-4.3 4.3m-18.2 18.2-4.3 4.3"/><rect x="14" y="15" width="20" height="18" rx="5"/><path d="M18 21h12M19 27h2m6 0h2M20 37h8"/><circle cx="24" cy="8" r="2"/></svg>
    </div>
    <div class="empty-copy"><strong>{{ title }}</strong><span>{{ message }}</span></div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: 'Nothing here yet' },
  message: { type: String, default: 'Check back soon for updates.' },
})
</script>

<style scoped>
.empty-state{grid-column:1/-1;display:flex;align-items:center;gap:15px;max-width:620px;margin:18px auto;padding:18px 22px;border:1px solid rgba(34,211,238,.18);border-radius:14px;background:linear-gradient(120deg,rgba(34,211,238,.055),rgba(245,158,11,.035));box-shadow:inset 0 1px rgba(255,255,255,.025)}
.empty-icon{display:grid;place-items:center;width:44px;height:44px;flex:0 0 44px;border:1px solid rgba(34,211,238,.25);border-radius:12px;color:var(--accent-cyan);background:rgba(34,211,238,.06)}.empty-icon svg{width:29px;height:29px;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}.empty-copy{display:grid;gap:4px}.empty-copy strong{font:1.1rem 'Bebas Neue',sans-serif;letter-spacing:.06em;color:var(--text-primary)}.empty-copy span{font-size:.83rem;color:var(--text-dim)}
</style>
