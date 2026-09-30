<template>
  <span class="status-badge" :class="`tone-${tone}`" :role="tone === 'error' ? 'alert' : 'status'" aria-live="polite">
    <span class="status-dot" aria-hidden="true"></span>
    <slot>{{ label }}</slot>
  </span>
</template>

<script setup>
defineProps({
  label: { type: String, default: '' },
  tone: { type: String, default: 'info' },
})
</script>

<style scoped>
.status-badge{display:inline-flex;align-items:center;gap:8px;width:max-content;max-width:100%;padding:6px 11px;border:1px solid currentColor;border-radius:999px;background:rgba(34,211,238,.07);font:500 .64rem 'DM Mono',monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--accent-cyan);line-height:1.25}
.status-dot{width:6px;height:6px;flex:0 0 6px;border-radius:50%;background:currentColor;box-shadow:0 0 9px currentColor}
.tone-success{color:var(--green,#4ade80);background:rgba(74,222,128,.08)}.tone-warning{color:var(--amber,#f59e0b);background:rgba(245,158,11,.08)}.tone-muted{color:var(--text-muted,#78869c);background:rgba(120,134,156,.08)}.tone-error{color:var(--rust,#fb7185);background:rgba(251,113,133,.08)}.tone-info{color:var(--accent-cyan,#22d3ee)}
</style>
