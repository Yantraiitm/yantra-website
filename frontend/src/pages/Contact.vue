<template>
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Contact</span></div>
      <span class="tag">// Get in touch</span>
      <h1 class="page-hero-title">Contact Us</h1>
      <p class="page-hero-sub">Have a question, collaboration idea, or just want to say hello? We'd love to hear from you.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="contact-info-grid reveal">
        <div class="contact-info-item">
          <div class="contact-icon">📧</div>
          <div>
            <div class="contact-info-label">Email</div>
            <div class="contact-info-value"><a href="mailto:yantra@study.iitm.ac.in">yantra@study.iitm.ac.in</a></div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon">💬</div>
          <div>
            <div class="contact-info-label">Discord</div>
            <div class="contact-info-value"><a href="https://discord.gg/nQtEpKy4eS" target="_blank">discord.gg/nQtEpKy4eS</a></div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon">💼</div>
          <div>
            <div class="contact-info-label">LinkedIn</div>
            <div class="contact-info-value"><a href="https://www.linkedin.com/company/yantra-iitm-bs-robotics-club" target="_blank">Yantra Robotics IITM</a></div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon">🐱</div>
          <div>
            <div class="contact-info-label">GitHub</div>
            <div class="contact-info-value"><a href="https://github.com/Yantraiitm" target="_blank">github.com/Yantraiitm</a></div>
          </div>
        </div>
        <div class="contact-info-item" style="grid-column:span 2;">
          <div class="contact-icon">📍</div>
          <div>
            <div class="contact-info-label">BS Program Office</div>
            <div class="contact-info-value">IIT Madras BS Degree Office, 3rd Floor ICSR Building, 600036</div>
          </div>
        </div>
      </div>

      <div class="reveal">
        <span class="tag" style="margin-bottom:16px;display:block;">// Common questions</span>
        <h3 style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;margin-bottom:20px;">FAQ</h3>
        <div style="display:flex;flex-direction:column;gap:16px;max-width:700px;">
          <div class="card" style="padding:20px;">
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">When can I join Yantra?</div>
            <p style="font-size:0.82rem;color:var(--text-dim);line-height:1.7;">We recruit members at the beginning of each semester. Check the Join page for current recruitment timelines.</p>
          </div>
          <div class="card" style="padding:20px;">
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Do I need experience?</div>
            <p style="font-size:0.82rem;color:var(--text-dim);line-height:1.7;">Not at all! We welcome complete beginners. Curiosity and enthusiasm matter more than prior knowledge.</p>
          </div>
          <div class="card" style="padding:20px;">
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Can external students collaborate?</div>
            <p style="font-size:0.82rem;color:var(--text-dim);line-height:1.7;">We occasionally partner with other institutions. Reach out via email to discuss collaboration opportunities.</p>
          </div>
          <div class="card" style="padding:20px;">
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">How do you select members?</div>
            <p style="font-size:0.82rem;color:var(--text-dim);line-height:1.7;">Through a short application form followed by a brief interview or a small technical task depending on the domain.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal.js'
useScrollReveal()
</script>
