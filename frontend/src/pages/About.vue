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
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-bottom:80px;">
        <div class="card reveal" style="border-left:3px solid var(--amber);">
          <div style="font-size:2.5rem;margin-bottom:16px;">🎯</div>
          <h3 style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;margin-bottom:12px;color:var(--amber);">Our Mission</h3>
          <p style="color:var(--text-dim);line-height:1.8;font-size:0.95rem;">Our mission is to foster innovation in robotics and automation by providing students with opportunities to build, experiment, and collaborate on advanced engineering projects. We believe in learning by doing — building real systems that solve real problems.</p>
        </div>
        <div class="card reveal" style="border-left:3px solid var(--rust);">
          <div style="font-size:2.5rem;margin-bottom:16px;">🚀</div>
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
          <div class="domain-icon">⚡</div>
          <div class="domain-title">Embedded Systems</div>
          <p class="domain-desc">Programming microcontrollers and designing real-time systems for robots and smart devices. We work with ESP32, STM32, Arduino, and RTOS platforms.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon">👁️</div>
          <div class="domain-title">Computer Vision</div>
          <p class="domain-desc">Developing intelligent vision systems for robot perception. Object detection, tracking, depth estimation, and scene understanding using OpenCV, PyTorch, and YOLO.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon">🧠</div>
          <div class="domain-title">Artificial Intelligence</div>
          <p class="domain-desc">Applying machine learning and AI techniques to autonomous systems. Reinforcement learning, neural networks, path planning, and decision-making algorithms.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon">⚙️</div>
          <div class="domain-title">Mechanical Design</div>
          <p class="domain-desc">Designing robot structures, mechanisms, and actuators. CAD modeling, 3D printing, structural analysis, and integration of mechanical systems with electronics.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon">📡</div>
          <div class="domain-title">IoT &amp; Connectivity</div>
          <p class="domain-desc">Building connected robotic systems with wireless communication, cloud integration, and real-time telemetry using MQTT, BLE, and Wi-Fi protocols.</p>
        </div>
        <div class="domain-card reveal">
          <div class="domain-icon">🔬</div>
          <div class="domain-title">Research &amp; Innovation</div>
          <p class="domain-desc">Pursuing novel research at the intersection of robotics, AI, and automation. Publishing technical reports and participating in academic competitions.</p>
        </div>
      </div>

      <div class="glow-line"></div>

      <span class="tag">// Our principles</span>
      <h2 class="section-title reveal">Core Values</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;">
        <div class="card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div style="font-size:1.8rem;flex-shrink:0;">💡</div>
          <div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Innovation</div>
            <p style="color:var(--text-dim);font-size:0.84rem;line-height:1.7;">We push boundaries and embrace creative problem-solving in every project we undertake.</p>
          </div>
        </div>
        <div class="card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div style="font-size:1.8rem;flex-shrink:0;">🤝</div>
          <div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;margin-bottom:6px;color:var(--amber);">Collaboration</div>
            <p style="color:var(--text-dim);font-size:0.84rem;line-height:1.7;">Cross-domain teams produce the best robots. We foster a culture of mutual learning.</p>
          </div>
        </div>
        <div class="card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div style="font-size:1.8rem;flex-shrink:0;">📚</div>
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
      <RouterLink to="/join" class="btn btn-primary">⚡ Apply Now</RouterLink>
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
