<template>
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>About</span></div>
      <span class="tag">// Who we are</span>
      <h1 class="page-hero-title">About Yantra</h1>
      <p class="page-hero-sub">The Official Robotics Society of IIT Madras BS Degree Program where engineering meets innovation.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="about-mission-grid">
        <div class="card reveal" style="border-left:3px solid var(--amber);">
          <div style="width:40px;height:40px;margin-bottom:16px;color:var(--amber);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></div>
          <h3 style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;margin-bottom:12px;color:var(--amber);">Our Mission</h3>
          <p style="color:var(--text-dim);line-height:1.8;font-size:0.95rem;">Our mission is to foster innovation in robotics and automation by providing students with opportunities to build, experiment, and collaborate on advanced engineering projects. We believe in learning by doing — building real systems that solve real problems.</p>
        </div>
        <div class="card reveal" style="border-left:3px solid var(--rust);">
          <div style="width:40px;height:40px;margin-bottom:16px;color:var(--rust);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 00-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 012-3.95A12.88 12.88 0 0122 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 01-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg></div>
          <h3 style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;margin-bottom:12px;color:var(--rust);">Our Vision</h3>
          <p style="color:var(--text-dim);line-height:1.8;font-size:0.95rem;">To become a leading student robotics community that drives innovation and contributes to the future of intelligent machines. We aim to produce engineers and researchers who shape the next era of autonomous systems.</p>
        </div>
      </div>

      <div class="glow-line"></div>

      <span class="tag">// Technical domains</span>
      <h2 class="section-title reveal">What We Work On</h2>
      <p class="section-subtitle reveal">Yantra spans multiple disciplines of modern engineering and computer science.</p>

      <div class="domain-grid">
        <div class="domain-card reveal">
          <div class="domain-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6v6H9z"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M18 9h3M3 15h3M18 15h3"/></svg></div>
          <div class="domain-title">Embedded Systems</div>
          <p class="domain-desc">Programming microcontrollers and designing real-time systems for robots and smart devices. We work with ESP32, STM32, Arduino, and RTOS platforms.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><ellipse cx="12" cy="12" rx="10" ry="6"/><circle cx="12" cy="12" r="3"/></svg></div>
          <div class="domain-title">Computer Vision</div>
          <p class="domain-desc">Developing intelligent vision systems for robot perception. Object detection, tracking, depth estimation, and scene understanding using OpenCV, PyTorch, and YOLO.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M12 7v4M12 11l-5 6M12 11l5 6"/></svg></div>
          <div class="domain-title">Artificial Intelligence</div>
          <p class="domain-desc">Applying machine learning and AI techniques to autonomous systems. Reinforcement learning, neural networks, path planning, and decision-making algorithms.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.22 4.22l2.12 2.12M17.66 17.66l2.12 2.12M2 12h3M19 12h3M4.22 19.78l2.12-2.12M17.66 6.34l2.12-2.12"/></svg></div>
          <div class="domain-title">Mechanical Design</div>
          <p class="domain-desc">Designing robot structures, mechanisms, and actuators. CAD modeling, 3D printing, structural analysis, and integration of mechanical systems with electronics.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12.55a11 11 0 0114.08 0"/><path d="M1.42 9a16 16 0 0121.16 0"/><path d="M8.53 16.11a6 6 0 016.95 0"/><circle cx="12" cy="20" r="1" fill="currentColor"/></svg></div>
          <div class="domain-title">IoT &amp; Connectivity</div>
          <p class="domain-desc">Building connected robotic systems with wireless communication, cloud integration, and real-time telemetry using MQTT, BLE, and Wi-Fi protocols.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 3H5a2 2 0 00-2 2v4m6-6h10a2 2 0 012 2v4M9 3v18m0 0h10a2 2 0 002-2V9M9 21H5a2 2 0 01-2-2V9m0 0h18"/></svg></div>
          <div class="domain-title">Research &amp; Innovation</div>
          <p class="domain-desc">Pursuing novel research at the intersection of robotics, AI, and automation. Publishing technical reports and participating in academic competitions.</p>
        </div>
      </div>

      <div class="glow-line"></div>

      <span class="tag">// Our principles</span>
      <h2 class="section-title reveal">Core Values</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;">
        <div class="card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div style="width:36px;height:36px;flex-shrink:0;color:var(--amber);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 006 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6M10 22h4"/></svg></div>
          <div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Innovation</div>
            <p style="color:var(--text-dim);font-size:0.84rem;line-height:1.7;">We push boundaries and embrace creative problem-solving in every project we undertake.</p>
          </div>
        </div>
        <div class="card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div style="width:36px;height:36px;flex-shrink:0;color:var(--amber);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
          <div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Collaboration</div>
            <p style="color:var(--text-dim);font-size:0.84rem;line-height:1.7;">Cross-domain teams produce the best robots. We foster a culture of mutual learning.</p>
          </div>
        </div>
        <div class="card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div style="width:36px;height:36px;flex-shrink:0;color:var(--amber);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg></div>
          <div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Continuous Learning</div>
            <p style="color:var(--text-dim);font-size:0.84rem;line-height:1.7;">Technology evolves fast. We grow faster through workshops, courses, and hands-on builds.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary);">
    <div class="container" style="text-align:center;">
      <h2 class="section-title reveal" style="margin-bottom:16px;">Ready to Build with Us?</h2>
      <p style="color:var(--text-dim);margin-bottom:32px;max-width:440px;margin-left:auto;margin-right:auto;">Whether you're a coder, maker, or dreamer — there's a place for you in Yantra.</p>
      <RouterLink to="/join" class="btn btn-primary">Apply Now →</RouterLink>
      &nbsp;&nbsp;
      <RouterLink to="/team" class="btn btn-ghost">Meet the Team →</RouterLink>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal.js'
useScrollReveal()
</script>
