<template>
  <!-- HERO -->
  <section class="hero">
    <div class="hero-glow-a"></div>
    <div class="hero-glow-b"></div>
    <div class="hero-stripe"></div>
    <div class="hero-inner">
      <div>
        <div class="hero-badge">
          <div class="badge-dot"></div>
          Robotics Society · IIT Madras BS Degree Program
        </div>
        <h1 class="hero-title">Yantra<br><span class="title-accent">ROBOTICS</span></h1>
        <p class="hero-tagline"><b>Build</b> · <b>Innovate</b> · <b>Automate</b></p>
        <p class="hero-desc">The premier student robotics society of IIT Madras BS. We design, build, and deploy real machines — combat bots, autonomous systems, AI vision platforms, and more.</p>
        <div class="hero-btns">
          <RouterLink to="/projects" class="btn btn-amber">Explore Projects</RouterLink>
          <RouterLink to="/join" class="btn btn-ghost">Apply to Join</RouterLink>
        </div>
      </div>
      <div class="hero-panel">
        <div class="status-card">
          <div class="sc-top">
            <span class="sc-label">Club Overview</span>
            <span class="sc-live"><div class="sc-live-dot"></div>Active · 2026</span>
          </div>
          <div class="sc-stats">
            <div class="sc-stat"><div class="sc-num">1200<sup>+</sup></div><div class="sc-lbl">Members</div></div>
            <div class="sc-stat"><div class="sc-num">40<sup>+</sup></div><div class="sc-lbl">Projects</div></div>
            <div class="sc-stat"><div class="sc-num">20<sup>+</sup></div><div class="sc-lbl">Workshops</div></div>
            <div class="sc-stat"><div class="sc-num">2<sup>+</sup></div><div class="sc-lbl">Competitions</div></div>
          </div>
          <div class="sc-chips">
            <div class="chip">⚡ Embedded</div>
            <div class="chip">👁 Vision</div>
            <div class="chip">🧠 AI / ML</div>
            <div class="chip">⚙ Mechanical</div>
            <div class="chip">📡 IoT</div>
          </div>
          <div class="sc-terminal">
            <span class="prompt">yantra@iitm-bs:~$ </span>robot.init()<br>
            <span style="color:var(--amber)">✓</span> sensors.online<br>
            <span style="color:var(--amber)">✓</span> systems.nominal<br>
            <span class="prompt">yantra@iitm-bs:~$ </span><span class="cursor"></span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MARQUEE -->
  <div class="marquee-wrap">
    <div class="marquee-track" aria-hidden="true">
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">ESP32</span> Embedded Systems</div>
      <div class="mi"><div class="mi-dot"></div>Computer <span class="mi-hi">Vision</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">FreeRTOS</span> Real-Time</div>
      <div class="mi"><div class="mi-dot"></div>Autonomous <span class="mi-hi">Navigation</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">ROS2</span> Framework</div>
      <div class="mi"><div class="mi-dot"></div>Deep <span class="mi-hi">Learning</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">SLAM</span> Mapping</div>
      <div class="mi"><div class="mi-dot"></div>Laser <span class="mi-hi">Battle Robots</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">ESP32</span> Embedded Systems</div>
      <div class="mi"><div class="mi-dot"></div>Computer <span class="mi-hi">Vision</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">FreeRTOS</span> Real-Time</div>
      <div class="mi"><div class="mi-dot"></div>Autonomous <span class="mi-hi">Navigation</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">ROS2</span> Framework</div>
      <div class="mi"><div class="mi-dot"></div>Deep <span class="mi-hi">Learning</span></div>
      <div class="mi"><div class="mi-dot"></div><span class="mi-hi">SLAM</span> Mapping</div>
      <div class="mi"><div class="mi-dot"></div>Laser <span class="mi-hi">Battle Robots</span></div>
    </div>
  </div>

  <!-- ABOUT -->
  <section class="section">
    <div class="container">
      <div class="about-grid">
        <div>
          <div class="eyebrow reveal">About Yantra</div>
          <h2 class="sec-title reveal">Engineering <em>the future</em>,<br>setting a benchmark everytime.</h2>
          <div class="about-text reveal">
            <p>Yantra is the Robotics Society of the IIT Madras BS Degree Program — a community of builders, coders, designers, and tinkerers united by one goal: making real things.</p>
            <p>Whether you start with zero experience or you've already built robots, Yantra accelerates your journey through projects, workshops, and competitions.</p>
          </div>
          <div style="margin-top:26px;" class="reveal">
            <RouterLink to="/about" class="btn btn-ghost">About us →</RouterLink>
          </div>
        </div>
        <div class="domains reveal">
          <div class="dom"><div class="dom-icon">⚡</div><div><div class="dom-name">Embedded</div><div class="dom-desc">MCUs, RTOS, PCB</div></div></div>
          <div class="dom"><div class="dom-icon">👁</div><div><div class="dom-name">Vision</div><div class="dom-desc">YOLO, OpenCV</div></div></div>
          <div class="dom"><div class="dom-icon">🧠</div><div><div class="dom-name">AI / ML</div><div class="dom-desc">RL, planning</div></div></div>
          <div class="dom"><div class="dom-icon">⚙</div><div><div class="dom-name">Mechanical</div><div class="dom-desc">CAD, 3D print</div></div></div>
          <div class="dom"><div class="dom-icon">📡</div><div><div class="dom-name">IoT</div><div class="dom-desc">MQTT, BLE</div></div></div>
          <div class="dom"><div class="dom-icon">🔬</div><div><div class="dom-name">Research</div><div class="dom-desc">Papers, R&D</div></div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- COLLABORATORS -->
  <section class="section section-alt">
    <div class="container">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:32px;flex-wrap:wrap;gap:14px;">
        <div>
          <div class="eyebrow reveal">Trusted By Industry Leaders</div>
          <h2 class="sec-title reveal">Our <em>Collaborators</em></h2>
        </div>
        <a href="mailto:yantra@study.iitm.ac.in" class="btn btn-ghost reveal" style="align-self:flex-end;">Become a Partner →</a>
      </div>
      <div class="collaborators-grid">
        <div class="collab-card reveal">
          <div class="collab-logo"><img src="/img/inidan_army.png" alt="Indian Army"></div>
          <div class="collab-body">
            <div class="collab-name">Indian Army</div>
            <p class="collab-desc">Defense robotics research and autonomous systems development</p>
            <div class="collab-tags"><span class="t-tag">Defense</span><span class="t-tag">R&D</span></div>
          </div>
        </div>
        <div class="collab-card reveal">
          <div class="collab-logo"><img src="/img/iitk.png" alt="IIT Kanpur"></div>
          <div class="collab-body">
            <div class="collab-name">IIT Kanpur</div>
            <p class="collab-desc">Joint research projects in AI and autonomous navigation systems</p>
            <div class="collab-tags"><span class="t-tag">Research</span><span class="t-tag">AI</span></div>
          </div>
        </div>
        <div class="collab-card reveal">
          <div class="collab-logo"><img src="/img/tech.png" alt="Techkriti"></div>
          <div class="collab-body">
            <div class="collab-name">Techkriti IITK</div>
            <p class="collab-desc">Annual tech festival collaboration for robotics showcase</p>
            <div class="collab-tags"><span class="t-tag">Events</span><span class="t-tag">Showcase</span></div>
          </div>
        </div>
        <div class="collab-card reveal">
          <div class="collab-logo"><img src="/img/para.png" alt="Paradox"></div>
          <div class="collab-body">
            <div class="collab-name">Paradox</div>
            <p class="collab-desc">Robotics Competition and showcase of project.</p>
            <div class="collab-tags"><span class="t-tag">Events</span><span class="t-tag">Competition</span></div>
          </div>
        </div>
        <div class="collab-card reveal">
          <div class="collab-logo"><img src="/img/hive.png" alt="HIVE IITK"></div>
          <div class="collab-body">
            <div class="collab-name">HIVE IITK</div>
            <p class="collab-desc">Research and development</p>
            <div class="collab-tags"><span class="t-tag">Research</span><span class="t-tag">Technology</span></div>
          </div>
        </div>
        <div class="collab-card reveal">
          <div class="collab-logo"><img src="/img/iitm.png" alt="IIT Madras"></div>
          <div class="collab-body">
            <div class="collab-name">IIT Madras</div>
            <p class="collab-desc">Academic partnership for robotics curriculum and research</p>
            <div class="collab-tags"><span class="t-tag">Academic</span><span class="t-tag">Research</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- INTERNSHIPS -->
  <section class="section section-alt">
    <div class="container">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:32px;flex-wrap:wrap;gap:14px;">
        <div>
          <div class="eyebrow reveal">Career Opportunities</div>
          <h2 class="sec-title reveal">Internships via <em>Yantra</em></h2>
        </div>
      </div>
      <div class="internships-grid">
        <div class="intern-card reveal"><div class="intern-logo"><img src="/img/hive.png" alt="HIVE"></div><div class="intern-body"><div class="intern-name">Ayush Sharma</div><div class="intern-role">AI/ML Programming Intern</div><div class="intern-company">HIVE IITK</div><div class="intern-tags"><span class="t-tag">AI</span><span class="t-tag">ML</span><span class="t-tag">Python</span></div></div></div>
        <div class="intern-card reveal"><div class="intern-logo"><img src="/img/inidan_army.png" alt="Army"></div><div class="intern-body"><div class="intern-name">Vivek Rawat</div><div class="intern-role">Robotics &amp; Electronics Intern</div><div class="intern-company">HIVE IITK and Indian Army</div><div class="intern-tags"><span class="t-tag">Robotics</span><span class="t-tag">Electronics</span></div></div></div>
        <div class="intern-card reveal"><div class="intern-logo"><img src="/img/hive.png" alt="HIVE"></div><div class="intern-body"><div class="intern-name">Aruthra</div><div class="intern-role">Robotics &amp; Electronics Intern</div><div class="intern-company">HIVE IITK</div><div class="intern-tags"><span class="t-tag">Robotics</span><span class="t-tag">Embedded</span></div></div></div>
        <div class="intern-card reveal"><div class="intern-logo"><img src="/img/hive.png" alt="HIVE"></div><div class="intern-body"><div class="intern-name">Ayush Singh</div><div class="intern-role">Electronics Engineering Intern</div><div class="intern-company">HIVE IITK</div><div class="intern-tags"><span class="t-tag">Electronics</span><span class="t-tag">PCB</span></div></div></div>
        <div class="intern-card reveal"><div class="intern-logo"><img src="/img/inidan_army.png" alt="Army"></div><div class="intern-body"><div class="intern-name">Akhilesh Bhagat</div><div class="intern-role">Electronics &amp; AI/ML Intern</div><div class="intern-company">HIVE IITK and Indian Army</div><div class="intern-tags"><span class="t-tag">Electronics</span><span class="t-tag">AI</span><span class="t-tag">ML</span></div></div></div>
        <div class="intern-card reveal"><div class="intern-logo"><img src="/img/hive.png" alt="HIVE"></div><div class="intern-body"><div class="intern-name">Kratika Jain</div><div class="intern-role">Music Technology Intern</div><div class="intern-company">HIVE IITK</div><div class="intern-tags"><span class="t-tag">Music Tech</span><span class="t-tag">HCI</span></div></div></div>
      </div>
    </div>
  </section>

  <!-- CONFERENCE PAPERS -->
  <section class="section">
    <div class="container">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:32px;flex-wrap:wrap;gap:14px;">
        <div>
          <div class="eyebrow reveal">Research Excellence</div>
          <h2 class="sec-title reveal">Papers in <em>Conferences</em></h2>
        </div>
      </div>
      <div class="papers-grid">
        <div class="paper-card reveal">
          <div class="paper-icon">📄</div>
          <div class="paper-body">
            <div class="paper-title">Gravitone: Space-Time Sonification Interface</div>
            <div class="paper-authors">Kratika Jain, Allwin Williams, Akhilesh Kumar Bhagat, et al.</div>
            <div class="paper-conference">NIME 2025 (New Interfaces for Musical Expression)</div>
            <div class="paper-meta"><span class="paper-status accepted">✓ Accepted</span><span class="paper-date">2025</span></div>
            <p class="paper-desc">Novel musical instrument using data sonification techniques inspired by space-time mesh models.</p>
            <div class="paper-tags"><span class="t-tag">Music Tech</span><span class="t-tag">Sonification</span><span class="t-tag">HCI</span></div>
            <a href="https://nime.org/proc/nime2025_95/index.html" class="paper-link" target="_blank">View Paper →</a>
          </div>
        </div>
        <div class="paper-card reveal">
          <div class="paper-icon">📄</div>
          <div class="paper-body">
            <div class="paper-title">Swaringz: Haptic Musical Performance System</div>
            <div class="paper-authors">Sumit Kumar, Soubhagya K Dev, Lakshmi Srinath, et al.</div>
            <div class="paper-conference">UIST 2025 (ACM Symposium on User Interface Software)</div>
            <div class="paper-meta"><span class="paper-status accepted">✓ Accepted</span><span class="paper-date">2025</span></div>
            <p class="paper-desc">Ergonomics-based instrument with haptic feedback enhancing intuitive musical interaction.</p>
            <div class="paper-tags"><span class="t-tag">Haptics</span><span class="t-tag">Music</span><span class="t-tag">UIST</span></div>
            <a href="https://dl.acm.org/doi/full/10.1145/3746058.3758455" class="paper-link" target="_blank">View Paper →</a>
          </div>
        </div>
        <div class="paper-card reveal">
          <div class="paper-icon">📄</div>
          <div class="paper-body">
            <div class="paper-title">Assistive HCI Frameworks for Motor-Impaired Users</div>
            <div class="paper-authors">Prakriti Mukherjee, Lakshmi Srinath, Kratika Jain, et al.</div>
            <div class="paper-conference">CHI 2026 (Conference on Human Factors in Computing)</div>
            <div class="paper-meta"><span class="paper-status accepted">✓ Accepted</span><span class="paper-date">2026</span></div>
            <p class="paper-desc">Research on accessible interfaces leveraging eye-gaze, gesture, and adaptive control systems.</p>
            <div class="paper-tags"><span class="t-tag">Accessibility</span><span class="t-tag">HCI</span><span class="t-tag">CHI</span></div>
            <a href="#" class="paper-link">View Paper →</a>
          </div>
        </div>
        <div class="paper-card reveal">
          <div class="paper-icon">📄</div>
          <div class="paper-body">
            <div class="paper-title">GraviTone: A Tangible Musical Interface using Gravity Well</div>
            <div class="paper-authors">Kratika Jain*, Allwin Williams, Akhilesh Kumar Bhagat, Sukanth K, et al.</div>
            <div class="paper-conference">India HCI 2024 (ID 227)</div>
            <div class="paper-meta"><span class="paper-status accepted">✓ Poster</span><span class="paper-date">2024</span></div>
            <p class="paper-desc">Tangible musical interface using gravity well for sound and music creation</p>
            <div class="paper-tags"><span class="t-tag">Music Tech</span><span class="t-tag">Tangible UI</span><span class="t-tag">Gravity</span></div>
            <a href="https://www.2025.indiahci.org/programme_1/posters-demos-artworks" class="paper-link" target="_blank">View Poster →</a>
          </div>
        </div>
        <div class="paper-card reveal">
          <div class="paper-icon">📄</div>
          <div class="paper-body">
            <div class="paper-title">Swarings: Exploring Expressive Freedom through Ring-Based Musical Interaction</div>
            <div class="paper-authors">Sumit Kumar, Soubhagya K Dev*, Lakshmi Srinath, Ashish Kumar, et al.</div>
            <div class="paper-conference">India HCI 2024 (ID 228)</div>
            <div class="paper-meta"><span class="paper-status accepted">✓ Poster</span><span class="paper-date">2024</span></div>
            <p class="paper-desc">Ring-based musical interaction system for expressive musical performance</p>
            <div class="paper-tags"><span class="t-tag">Music</span><span class="t-tag">Wearable</span><span class="t-tag">Ring</span></div>
            <a href="https://www.2025.indiahci.org/programme_1/posters-demos-artworks" class="paper-link" target="_blank">View Poster →</a>
          </div>
        </div>
        <div class="paper-card reveal">
          <div class="paper-icon">📄</div>
          <div class="paper-body">
            <div class="paper-title">The Tabla Glove: An Accompanist for Musical Training and Exploration</div>
            <div class="paper-authors">Prakriti Mukherjee*, Lakshmi Srinath, Kratika Jain, et al.</div>
            <div class="paper-conference">India HCI 2024 (ID 229)</div>
            <div class="paper-meta"><span class="paper-status accepted">✓ Poster</span><span class="paper-date">2024</span></div>
            <p class="paper-desc">Smart glove system for tabla training and musical exploration</p>
            <div class="paper-tags"><span class="t-tag">Tabla</span><span class="t-tag">Glove</span><span class="t-tag">Training</span></div>
            <a href="https://www.2025.indiahci.org/programme_1/posters-demos-artworks" class="paper-link" target="_blank">View Poster →</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- EVENTS -->
  <section class="section">
    <div class="container">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:32px;flex-wrap:wrap;gap:14px;">
        <div>
          <div class="eyebrow reveal">What's on</div>
          <h2 class="sec-title reveal">Upcoming <em>Events</em></h2>
        </div>
        <RouterLink to="/events" class="btn btn-ghost reveal" style="align-self:flex-end;">All events →</RouterLink>
      </div>
      <div class="events-stack">
        <div class="ev reveal">
          <div class="ev-cal"><div class="ev-day">18</div><div class="ev-mo">Mar</div></div>
          <div>
            <div class="ev-type">▶ Workshop</div>
            <div class="ev-name">Embedded Systems Workshop</div>
            <div class="ev-info">GPIO, UART &amp; FreeRTOS hands-on · <b>Prof. Viveka K R</b></div>
          </div>
          <RouterLink to="/events" class="btn btn-ghost" style="font-size:0.62rem;padding:9px 16px;white-space:nowrap;">Register →</RouterLink>
        </div>
        <div class="ev reveal">
          <div class="ev-cal"><div class="ev-day">05</div><div class="ev-mo">Apr</div></div>
          <div>
            <div class="ev-type">▶ Hackathon</div>
            <div class="ev-name">Robotics Hackathon 2026</div>
            <div class="ev-info">24-hour build · <b>₹10k prize · Teams of 2–4</b></div>
          </div>
          <RouterLink to="/events" class="btn btn-amber" style="font-size:0.62rem;padding:9px 16px;white-space:nowrap;">Register →</RouterLink>
        </div>
        <div class="ev reveal">
          <div class="ev-cal"><div class="ev-day">22</div><div class="ev-mo">Apr</div></div>
          <div>
            <div class="ev-type">▶ Guest Lecture</div>
            <div class="ev-name">AI in Modern Robotics</div>
            <div class="ev-info">Foundation models meet real robots · <b>Free entry</b></div>
          </div>
          <RouterLink to="/events" class="btn btn-ghost" style="font-size:0.62rem;padding:9px 16px;white-space:nowrap;">Notify me →</RouterLink>
        </div>
      </div>
    </div>
  </section>

  <!-- JOIN CTA -->
  <section class="section section-alt">
    <div class="container">
      <div class="cta-box reveal">
        <div class="cta-glow"></div>
        <h2 class="cta-title">Ready to <span>build</span> something real?</h2>
        <p class="cta-desc">No experience needed — just curiosity. Join Yantra and work on projects that actually ship, compete, and teach you more than any textbook can.</p>
        <div class="cta-btns">
          <RouterLink to="/join" class="btn btn-amber" style="padding:13px 30px;font-size:0.76rem;">Apply Now →</RouterLink>
          <RouterLink to="/contact" class="btn btn-ghost" style="padding:13px 30px;font-size:0.76rem;">Get in Touch</RouterLink>
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
