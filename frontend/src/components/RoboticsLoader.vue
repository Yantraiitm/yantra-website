<template>
  <div class="robot-loader" :class="{ compact, fullscreen }" role="status" aria-live="polite">
    <div class="robot-stage" aria-hidden="true">
      <div class="robot-track"></div>
      <svg class="robot" viewBox="0 0 80 80" fill="none">
        <path class="antenna" d="M40 13V7m0 0-5 4m5-4 5 4" />
        <circle class="signal" cx="40" cy="6" r="2" />
        <rect class="head" x="19" y="16" width="42" height="34" rx="10" />
        <path class="brow" d="M26 26h28" />
        <rect class="eye" x="27" y="31" width="9" height="8" rx="3" />
        <rect class="eye eye-second" x="44" y="31" width="9" height="8" rx="3" />
        <path class="mouth" d="M32 44h16" />
        <path class="neck" d="M35 51v6m10-6v6" />
        <path class="body" d="M23 58h34l5 12H18l5-12Z" />
        <path class="panel" d="M31 62h18" />
        <circle class="core" cx="40" cy="66" r="2" />
        <path class="arm arm-left" d="m20 59-7 6m47-6 7 6" />
      </svg>
      <span class="loader-orbit orbit-one"></span>
      <span class="loader-orbit orbit-two"></span>
    </div>
    <span class="loader-label">{{ label }}</span>
    <span v-if="!compact" class="loader-progress" aria-hidden="true"><i></i></span>
  </div>
</template>

<script setup>
defineProps({
  label: { type: String, default: 'Loading systems' },
  compact: { type: Boolean, default: false },
  fullscreen: { type: Boolean, default: false },
})
</script>

<style scoped>
.robot-loader{--robot-cyan:var(--accent-cyan,#22d3ee);--robot-amber:var(--amber,#f59e0b);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;min-height:180px;color:var(--text-dim,#b7c4d8)}
.robot-loader.fullscreen{position:fixed;inset:0;z-index:9998;min-height:100vh;gap:18px;background:radial-gradient(ellipse at center,rgba(8,28,45,.98),rgba(4,8,16,.99) 70%)}
.robot-stage{position:relative;width:102px;height:90px;display:grid;place-items:center}
.robot{position:relative;z-index:2;width:76px;height:76px;overflow:visible;animation:robot-bob 1.8s ease-in-out infinite}
.robot path,.robot rect{stroke:var(--robot-cyan);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.head,.body{fill:rgba(34,211,238,.08)}.brow,.mouth,.neck,.panel,.antenna{fill:none}.brow,.mouth{stroke:var(--robot-amber)!important}.eye{fill:var(--robot-cyan);stroke:none!important;animation:eye-pulse 1.3s ease-in-out infinite}.eye-second{animation-delay:.18s}.core,.signal{fill:var(--robot-amber);animation:eye-pulse .9s ease-in-out infinite}.signal{transform-origin:40px 6px}.robot-track{position:absolute;bottom:8px;width:88px;height:16px;border-bottom:1px solid rgba(34,211,238,.35);border-radius:50%;box-shadow:0 8px 12px -12px var(--robot-cyan)}
.loader-orbit{position:absolute;border:1px solid rgba(34,211,238,.28);border-radius:50%;transform:rotate(-25deg)}.orbit-one{width:96px;height:38px;animation:orbit 3s linear infinite}.orbit-two{width:82px;height:30px;border-color:rgba(245,158,11,.25);animation:orbit 2.4s linear infinite reverse}.loader-label{font:500 .68rem 'DM Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--robot-cyan);text-align:center}.loader-progress{width:150px;height:2px;overflow:hidden;background:rgba(148,163,184,.18)}.loader-progress i{display:block;width:40%;height:100%;background:linear-gradient(90deg,var(--robot-cyan),var(--robot-amber));animation:scan 1.5s ease-in-out infinite}
.compact{min-height:36px;flex-direction:row;justify-content:flex-start;gap:9px}.compact .robot-stage{width:34px;height:30px}.compact .robot{width:30px;height:30px}.compact .robot-track{width:31px;height:8px;bottom:0}.compact .loader-orbit{width:32px;height:12px}.compact .orbit-two{width:28px;height:10px}.compact .loader-label{font-size:.62rem}.compact .loader-progress{display:none}
@keyframes robot-bob{0%,100%{transform:translateY(1px)}50%{transform:translateY(-4px)}}@keyframes orbit{to{transform:rotate(335deg)}}@keyframes eye-pulse{0%,100%{opacity:.55}50%{opacity:1;filter:drop-shadow(0 0 4px var(--robot-cyan))}}@keyframes scan{0%{transform:translateX(-110%)}100%{transform:translateX(360%)}}
@media(prefers-reduced-motion:reduce){.robot,.loader-orbit,.loader-progress i,.eye,.signal{animation:none}}
</style>
