<template>
  <div>
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Join</span></div>
        <span class="tag">// Application</span>
        <h1 class="page-hero-title">Join Yantra</h1>
        <p class="page-hero-sub">Be part of IIT Madras BS's premier robotics society. Apply below to join the revolution.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">

        <div class="why-grid">
          <div class="why-card reveal">
            <div class="why-icon">🚀</div>
            <div class="why-title">Real Projects</div>
            <p class="why-desc">Build actual robots that compete and solve real problems.</p>
          </div>
          <div class="why-card reveal">
            <div class="why-icon">📚</div>
            <div class="why-title">Learn Fast</div>
            <p class="why-desc">Structured workshops and mentorship from experienced members.</p>
          </div>
          <div class="why-card reveal">
            <div class="why-icon">🏆</div>
            <div class="why-title">Compete</div>
            <p class="why-desc">Represent Yantra in national and international competitions.</p>
          </div>
          <div class="why-card reveal">
            <div class="why-icon">🤝</div>
            <div class="why-title">Network</div>
            <p class="why-desc">Connect with passionate engineers and industry mentors.</p>
          </div>
        </div>

        <div class="join-layout">

          <div class="reveal">
            <span class="tag">// What we look for</span>
            <h2 class="section-title" style="margin-bottom:14px;">Who Should <em style="color:var(--amber);font-style:normal;">Apply?</em></h2>
            <p style="color:var(--text-dim);font-size:0.88rem;line-height:1.85;margin-bottom:22px;font-weight:300;">
              We welcome students at all experience levels. Whether you've never soldered a wire
              or you've already built robots — if you're curious and passionate, we want you.
            </p>

            <div class="checklist">
              <div class="check-item"><span class="check-item-tick">✓</span> Passionate about robotics, AI, or hardware</div>
              <div class="check-item"><span class="check-item-tick">✓</span> Eager to learn and collaborate</div>
              <div class="check-item"><span class="check-item-tick">✓</span> IIT Madras BS Degree student</div>
              <div class="check-item"><span class="check-item-tick">✓</span> Ready to contribute time and effort</div>
              <div class="check-item"><span class="check-item-tick">✓</span> No prior experience required</div>
            </div>

            <div class="timeline-box">
              <div class="timeline-title">Join CORE Team</div>
              <div class="timeline-row">
                <span class="timeline-label">Mail interested position with CV</span>
                <span class="timeline-value">yantr@study.iitm.ac.in</span>
              </div>
              <div class="timeline-row">
                <span class="timeline-label">Follow Up mail if no reply</span>
                <span class="timeline-value">30 Days</span>
              </div>
              <div class="timeline-row">
                <span class="timeline-label">Fix interview date</span>
                <span class="timeline-value">Within 15 Days</span>
              </div>
              <div class="timeline-row">
                <span class="timeline-label">Results Announced</span>
                <span class="timeline-value">Within 15 Days</span>
              </div>
            </div>

            <div style="margin-top:22px;">
              <a
                href="https://docs.google.com/forms/d/e/1FAIpQLSdr09OVhgcKdH_KiaX3hJP55ECt6Gf0krkwLOVzlP9b9BYDcw/viewform"
                target="_blank"
                rel="noopener"
                class="btn btn-outline"
                style="width:100%;justify-content:center;font-size:0.68rem;"
              >
                ↗ Open Form in New Tab
              </a>
            </div>
          </div>

          <div class="form-wrap reveal">
            <div class="form-topbar">
              <div class="form-topbar-left">
                <div class="form-topbar-dot" style="background:#EA580C;"></div>
                <div class="form-topbar-dot" style="background:#F59E0B;"></div>
                <div class="form-topbar-dot" style="background:#4ADE80;"></div>
                <span class="form-topbar-title" style="margin-left:8px;">Yantra — Application Form</span>
              </div>
              <div class="form-topbar-actions">
                <a
                  href="https://docs.google.com/forms/d/e/1FAIpQLSdr09OVhgcKdH_KiaX3hJP55ECt6Gf0krkwLOVzlP9b9BYDcw/viewform"
                  target="_blank"
                  rel="noopener"
                  class="btn-open-new"
                  title="Open in new tab"
                >
                  <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5"/>
                    <path d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0z"/>
                  </svg>
                  Open in New Tab
                </a>
              </div>
            </div>

            <div class="form-iframe-wrap">
              <div class="form-loading" :class="{ hidden: formLoaded }" id="formLoader">
                <div class="form-loading-ring"></div>
                <div class="form-loading-text">Loading application form...</div>
              </div>
              <iframe
                class="google-form-iframe"
                src="https://docs.google.com/forms/d/e/1FAIpQLSdr09OVhgcKdH_KiaX3hJP55ECt6Gf0krkwLOVzlP9b9BYDcw/viewform?embedded=true"
                title="Yantra Application Form"
                loading="lazy"
                @load="onIframeLoad"
              >Loading…</iframe>
            </div>
          </div>

        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal'

useScrollReveal()

const formLoaded = ref(false)

function onIframeLoad() {
  formLoaded.value = true
}

onMounted(() => {
  setTimeout(() => { formLoaded.value = true }, 5000)
})
</script>

<style scoped>
.why-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 14px;
  margin-bottom: 64px;
}
.why-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 22px 18px;
  text-align: center;
  transition: var(--transition);
}
.why-card:hover { border-color: var(--border-glow); transform: translateY(-4px); }
.why-icon { font-size: 1.8rem; margin-bottom: 10px; }
.why-title {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: var(--amber);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.why-desc { font-size: 0.78rem; color: var(--text-dim); line-height: 1.6; font-weight: 300; }

.join-layout {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 48px;
  align-items: start;
}
@media (max-width: 900px) { .join-layout { grid-template-columns: 1fr; } }

.checklist { display: flex; flex-direction: column; gap: 10px; margin-bottom: 28px; }
.check-item {
  display: flex;
  gap: 11px;
  align-items: flex-start;
  font-size: 0.84rem;
  color: var(--text-dim);
  font-weight: 300;
  line-height: 1.5;
}
.check-item-tick { color: #4ADE80; flex-shrink: 0; font-size: 0.9rem; margin-top: 1px; }

.timeline-box {
  background: rgba(245,158,11,0.04);
  border: 1px solid rgba(245,158,11,0.18);
  border-radius: 9px;
  padding: 18px 20px;
  position: relative;
  overflow: hidden;
}
.timeline-box::before {
  content: '';
  position: absolute; top:0; left:10%; right:10%; height:1px;
  background: linear-gradient(90deg, transparent, var(--amber), transparent);
}
.timeline-title {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: var(--amber);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.timeline-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 7px 0;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  font-size: 0.8rem;
}
.timeline-row:last-child { border-bottom: none; }
.timeline-label { color: var(--text-muted); font-weight: 300; font-size: 0.78rem; }
.timeline-value { color: var(--text-primary); font-family: 'DM Mono', monospace; font-size: 0.7rem; }

.form-wrap {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
}
.form-wrap::before {
  content: '';
  position: absolute; top:0; left:12%; right:12%; height:1px;
  background: linear-gradient(90deg, transparent, var(--amber), transparent);
  z-index: 2;
}
.form-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 22px;
  background: var(--panel);
  border-bottom: 1px solid var(--border);
  position: relative;
  z-index: 1;
}
.form-topbar-left { display: flex; align-items: center; gap: 10px; }
.form-topbar-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.form-topbar-title {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: var(--text-muted);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.form-topbar-actions { display: flex; gap: 8px; }
.btn-open-new {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 5px;
  font-family: 'DM Mono', monospace;
  font-size: 0.6rem;
  color: var(--text-muted);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: border-color var(--transition), color var(--transition), background var(--transition);
  text-decoration: none;
}
.btn-open-new:hover { border-color: var(--amber); color: var(--amber); background: rgba(245,158,11,0.06); }
.btn-open-new svg { width: 11px; height: 11px; fill: currentColor; }

.form-iframe-wrap {
  position: relative;
  background: #1a1a1a;
}
.form-iframe-wrap::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(245,158,11,0.4), transparent);
  pointer-events: none;
  z-index: 1;
}
.google-form-iframe {
  display: block;
  width: 100%;
  height: 900px;
  border: none;
  filter: invert(93%) hue-rotate(180deg) saturate(0.9) brightness(0.92);
  background: #1c1c1c;
}
.form-loading {
  position: absolute;
  inset: 0;
  background: var(--bg-card);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  z-index: 5;
  transition: opacity 0.5s ease, visibility 0.5s ease;
}
.form-loading.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
.form-loading-ring {
  width: 40px; height: 40px;
  border: 2px solid var(--muted);
  border-top-color: var(--amber);
  border-right-color: var(--rust);
  border-radius: 50%;
  animation: formSpin 0.9s linear infinite;
}
.form-loading-text {
  font-family: 'DM Mono', monospace;
  font-size: 0.62rem;
  color: var(--text-muted);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
@keyframes formSpin { to { transform: rotate(360deg); } }
@media (max-width: 640px) {
  .google-form-iframe { height: 1100px; }
}
</style>
