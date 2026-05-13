<template>
  <div>
    <section class="section" style="padding-top: 120px;">
      <div class="container">

        <span class="tag">// Latest Updates</span>
        <h2 class="section-title reveal">From Instagram</h2>

        <div class="reveal" style="margin-bottom:64px;">
          <div class="elfsight-app-cae69c30-511d-4b2f-ac1f-8f7318cdd336"></div>
        </div>

        <div style="text-align:center; margin-bottom:64px;" class="reveal">
          <a
            href="https://www.instagram.com/yantra_iitm/"
            target="_blank"
            class="btn"
            style="background:linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); color:white; border:none;"
          >
            Explore more @yantra_iitm on Instagram →
          </a>
        </div>

        <span class="tag">// Previous events</span>
        <h2 class="section-title reveal">Past Events</h2>
        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:20px;">

          <div class="card reveal" style="opacity:0.7;">
            <div style="display:flex; gap:12px; align-items:center; margin-bottom:12px;">
              <div style="font-size:1.6rem;">🔧</div>
              <div>
                <div style="font-family:'Orbitron',sans-serif; font-size:0.8rem; font-weight:700;">Live Talk</div>
                <div style="font-family:'Share Tech Mono',monospace; font-size:0.68rem; color:var(--text-muted);">Deputy Chief Of Design @ The ePlane Co.</div>
              </div>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim);">Introduction to Arduino and ESP32 for absolute beginners. Students built a sensor display project.</p>
          </div>

          <div class="card reveal" style="opacity:0.7;">
            <div style="display:flex; gap:12px; align-items:center; margin-bottom:12px;">
              <div style="font-size:1.6rem;">⚡</div>
              <div>
                <div style="font-family:'Orbitron',sans-serif; font-size:0.8rem; font-weight:700;">Winter Robotics Hackathon</div>
                <div style="font-family:'Share Tech Mono',monospace; font-size:0.68rem; color:var(--text-muted);">Dec 2024 · 12 Teams</div>
              </div>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim);">12 teams competed over 24 hours. Winner built an autonomous path-planning robot using SLAM.</p>
          </div>

          <div class="card reveal" style="opacity:0.7;">
            <div style="display:flex; gap:12px; align-items:center; margin-bottom:12px;">
              <div style="font-size:1.6rem;">🎤</div>
              <div>
                <div style="font-family:'Orbitron',sans-serif; font-size:0.8rem; font-weight:700;">ROS2 Guest Lecture</div>
                <div style="font-family:'Share Tech Mono',monospace; font-size:0.68rem; color:var(--text-muted);">Nov 2024 · 80+ Attendees</div>
              </div>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim);">ROS2 framework intro by a Yantra alumnus now working at a robotics startup in Bengaluru.</p>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useScrollReveal } from '../composables/useScrollReveal'

useScrollReveal()

onMounted(() => {
  if (!document.querySelector('script[src*="elfsight"]')) {
    const script = document.createElement('script')
    script.src = 'https://static.elfsight.com/platform/platform.js'
    script.async = true
    document.head.appendChild(script)
  }
})
</script>
