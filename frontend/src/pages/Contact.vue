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
          <div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div>
          <div>
            <div class="contact-info-label">Email</div>
            <div class="contact-info-value"><a href="mailto:yantra@study.iitm.ac.in">yantra@study.iitm.ac.in</a></div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div>
          <div>
            <div class="contact-info-label">Discord</div>
            <div class="contact-info-value"><a href="https://discord.gg/nQtEpKy4eS" target="_blank">discord.gg/nQtEpKy4eS</a></div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg></div>
          <div>
            <div class="contact-info-label">LinkedIn</div>
            <div class="contact-info-value"><a href="https://www.linkedin.com/company/yantra-iitm-bs-robotics-club" target="_blank">Yantra Robotics IITM</a></div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg></div>
          <div>
            <div class="contact-info-label">GitHub</div>
            <div class="contact-info-value"><a href="https://github.com/Yantraiitm" target="_blank">github.com/Yantraiitm</a></div>
          </div>
        </div>
        <div class="contact-info-item" style="grid-column:span 2;">
          <div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
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
