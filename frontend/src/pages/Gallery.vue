<template>
  <div>
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Gallery</span></div>
        <span class="tag">// Moments captured</span>
        <h1 class="page-hero-title">Gallery</h1>
        <p class="page-hero-sub">Workshops, robot builds, competitions, and team memories from Yantra.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">

        <div class="filter-tabs">
          <button
            v-for="tab in tabs"
            :key="tab.value"
            class="filter-tab"
            :class="{ active: activeFilter === tab.value }"
            @click="activeFilter = tab.value"
          >{{ tab.label }}</button>
        </div>

        <template v-if="activeFilter === 'all' || activeFilter === 'workshops'">
          <span class="tag">// Workshops</span>
          <h2 class="section-title reveal" style="margin-bottom:24px;">Workshop Sessions</h2>
          <div class="gallery-grid-main" style="margin-bottom:48px;">
            <div class="gallery-item-main large reveal">
              <img src="/img/gallery/workshop_1.jpeg" alt="Drone Workshop">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Drone Workshop at 8 maratha LI</div>
                <div class="gallery-overlay-sub">2025 · 20 participants</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Workshop_4.png" alt="The ePlane Company CDO">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">The ePlane Company CDO</div>
                <div class="gallery-overlay-sub">2026 · Discussion</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Workshop_3.jpeg" alt="Online Workshop">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Online Workshop</div>
                <div class="gallery-overlay-sub">2025 · Intro to</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Workshop_2(1).jpeg" alt="Workshop @paradox">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Workshop @paradox</div>
                <div class="gallery-overlay-sub">2025 · Brainstorm</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Workshop_5.jpeg" alt="Robotics for students">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Robotics for students</div>
                <div class="gallery-overlay-sub">2025 · Hands-on</div>
              </div>
            </div>
          </div>
        </template>

        <template v-if="activeFilter === 'all' || activeFilter === 'robots'">
          <span class="tag">// Robots</span>
          <h2 class="section-title reveal" style="margin-bottom:24px;">Robot Builds</h2>
          <div class="gallery-grid-main" style="margin-bottom:48px;">
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/proj_1.jpg" alt="Dice Ball">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Dice Ball</div>
                <div class="gallery-overlay-sub">IIT Kanpur HIVE lab</div>
              </div>
            </div>
            <div class="gallery-item-main large reveal">
              <img src="/img/gallery/proj_3.jpg" alt="Working on swarings">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Working on swarings</div>
                <div class="gallery-overlay-sub">IIT Kanpur HIVE lab</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/proj_2.jpg" alt="VR mouth Tracker">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">VR mouth Tracker</div>
                <div class="gallery-overlay-sub">IIT Kanpur HIVE lab</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/proj_4.jpg" alt="Custom PCB v2">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Custom PCB v2</div>
                <div class="gallery-overlay-sub">IIT Kanpur HIVE lab</div>
              </div>
            </div>
          </div>
        </template>

        <template v-if="activeFilter === 'all' || activeFilter === 'competitions'">
          <span class="tag">// Competitions</span>
          <h2 class="section-title reveal" style="margin-bottom:24px;">Competition Highlights</h2>
          <div class="gallery-grid-main" style="margin-bottom:48px;">
            <div class="gallery-item-main large reveal">
              <img src="/img/gallery/Comp_2.jpeg" alt="RRCC">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">RRCC</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Comp_1.jpeg" alt="RRCC">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">RRCC</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Comp_5.jpeg" alt="RRCC">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">RRCC</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Comp_3.png" alt="RRCC">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">RRCC</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
          </div>
        </template>

        <template v-if="activeFilter === 'all' || activeFilter === 'team'">
          <span class="tag">// Team</span>
          <h2 class="section-title reveal" style="margin-bottom:24px;">Team Activities</h2>
          <div class="gallery-grid-main">
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Team_2.jpeg" alt="Meetup with Ms Bharti @ IITK">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Meetup with Ms Bharti @ IITK</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Team_3.jpeg" alt="Meetup @ paradox">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Meetup @ paradox</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
            <div class="gallery-item-main large reveal">
              <img src="/img/gallery/Team_1.jpeg" alt="RRCC Backend">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">RRCC Backend</div>
                <div class="gallery-overlay-sub">updating backend</div>
              </div>
            </div>
            <div class="gallery-item-main reveal">
              <img src="/img/gallery/Team_4.jpeg" alt="Meetup with Prof Jankiraman">
              <div class="gallery-overlay">
                <div class="gallery-overlay-title">Meetup with Prof Jankiraman</div>
                <div class="gallery-overlay-sub"></div>
              </div>
            </div>
          </div>
        </template>

      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal'

useScrollReveal()

const activeFilter = ref('all')
const tabs = [
  { value: 'all', label: 'All' },
  { value: 'workshops', label: 'Workshops' },
  { value: 'robots', label: 'Robots' },
  { value: 'competitions', label: 'Competitions' },
  { value: 'team', label: 'Team' },
]
</script>

<style scoped>
.gallery-grid-main {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}
.gallery-item-main {
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 4/3;
  background: linear-gradient(135deg, rgba(59,130,246,0.12), rgba(6,182,212,0.08));
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid var(--border);
}
.gallery-item-main img {
  width: 100%; height: 100%;
  object-fit: cover;
  position: absolute;
  inset: 0;
}
.gallery-item-main:hover {
  transform: scale(1.03);
  border-color: var(--border-glow);
  box-shadow: 0 8px 32px rgba(59,130,246,0.2);
}
.gallery-item-main.large {
  grid-column: span 2;
  aspect-ratio: 16/9;
}
.gallery-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(10,15,31,0.95) 0%, transparent 60%);
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  opacity: 0;
  transition: opacity 0.3s;
}
.gallery-item-main:hover .gallery-overlay { opacity: 1; }
.gallery-overlay-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 4px;
}
.gallery-overlay-sub {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.68rem;
  color: var(--accent-cyan);
  letter-spacing: 0.1em;
}
@media (max-width: 640px) {
  .gallery-item-main.large { grid-column: span 1; }
}
</style>
