<template>
  <div>
    <section class="page-hero team-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Team</span></div>
        <span class="tag">// The people</span>
        <h1 class="page-hero-title">Team Yantra</h1>
        <p class="page-hero-sub">The makers, mentors, and operators powering Yantra Robotics Society.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="team-grid team-grid-feature">
          <article
            v-for="member in teamMembers"
            :key="member.id"
            class="team-card team-card-modern reveal"
          >
            <div class="team-media">
              <img :src="member.image" :alt="`${member.role} profile photo`">
              <div class="team-scanline"></div>
              <span class="team-status">Active</span>
            </div>

            <div class="team-card-body">
              <p class="team-role" style="font-size: medium;">{{ member.role }}</p>
              <h3 class="team-name">{{ member.name }}</h3>
              <p class="team-desc">{{ member.description }}</p>

              <div class="team-skills">
                <span
                  v-for="skill in member.skills"
                  :key="skill"
                  class="skill-chip"
                >{{ skill }}</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal'

useScrollReveal()

const teamMembers = [
  {
    name: 'Sayed Zainuddin',
    role: 'Session Host',
    id: 1,
    image: '/img/team/sessionhost.png',
    description: 'Guides robotics sessions, keeps demos moving, and helps participants stay locked into the build.',
    skills: ['Hosting', 'Workshops', 'Robotics'],
  },
  {
    name: 'Kaushik Harsha',
    role: 'Web Dev Lead',
    id: 2,
    image: '/img/team/webdev.png',
    description: 'Leads web development and ensures the Yantra site stays polished, responsive, and performance-optimized.',
    skills: ['Frontend/UX', 'Vue.js', 'Flask'],
  },
  {
    name: 'Melvin Joseph',
    role: 'Management Tech Team Head',
    id: 3,
    image: '/img/team/management.png',
    description: 'Drives management technology strategy while aligning Yantra operations with scalable, intelligent systems.',
    skills: ['Management', 'Technology', 'Strategy'],
  },
  {
    name: 'Ajmal M S',
    role: 'Technical',
    id: 4,
    image: '/img/team/ajmaltech.jpeg',
    description: 'Specializes in technical engineering and robotics prototyping.',
    skills: ['Engineering', 'Robotics', 'Prototyping'],
  },
  {
    name: 'Anirban Mandal',
    role: 'Technical',
    id: 5,
    image: '/img/team/anirbantech.jpeg',
    description: 'Focuses on technical development and system integration.',
    skills: ['Development', 'Integration', 'Robotics'],
  },
  {
    name: 'Aryan',
    role: 'Technical',
    id: 6,
    image: '/img/team/aryantech.jpeg',
    description: 'Contributes to technical innovation and project execution.',
    skills: ['Innovation', 'Project Management', 'Robotics'],
  },
  {
    name: 'Jishnu Teja Dandamudi',
    role: 'Research',
    id: 7,
    image: '/img/team/jishnuresearch.jpeg',
    description: 'Leads research initiatives for advanced robotics solutions.',
    skills: ['Research', 'Innovation', 'Analysis'],
  },
]
</script>

<style scoped>
.team-hero::after {
  content: '';
  position: absolute;
  right: 8%;
  bottom: -1px;
  width: min(420px, 55vw);
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(245, 158, 11, 0.8), transparent);
}

.team-section-head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 32px;
  margin-bottom: 30px;
}

.team-section-head p {
  max-width: 520px;
  color: var(--text-dim);
  font-size: 0.98rem;
  line-height: 1.8;
  font-weight: 300;
  letter-spacing: 0.01em;
}

.team-grid-feature {
  grid-template-columns: repeat(auto-fit, minmax(280px, 360px));
}

.team-card-modern {
  padding: 0;
  overflow: hidden;
  text-align: left;
  background:
    linear-gradient(145deg, rgba(245, 158, 11, 0.08), transparent 38%),
    var(--bg-card);
  position: relative;
  max-height: 520px;
}

.team-card-modern::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  border: 1px solid transparent;
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.35), transparent 30%, rgba(74, 222, 128, 0.16)) border-box;
  mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  opacity: 0.6;
}

.team-media {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 57%;
  background: linear-gradient(135deg, #090b14, #111827);
  border-bottom: 1px solid var(--border);
  /* aspect-ratio: 2/3; */
  /* max-height: 260px; */
}

.team-media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: transparent;
  filter: saturate(0.96) contrast(1.04);
  transition: transform var(--transition), filter var(--transition);
}

.team-card-modern:hover .team-media img {
  transform: scale(1.04);
  filter: saturate(1.08) contrast(1.08);
}

.team-scanline {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(to bottom, transparent, rgba(245, 158, 11, 0.08), transparent),
    repeating-linear-gradient(to bottom, transparent 0 8px, rgba(255, 255, 255, 0.025) 9px);
  mix-blend-mode: screen;
  pointer-events: none;
}

.team-status {
  position: absolute;
  top: 14px;
  left: 14px;
  padding: 5px 10px;
  border: 1px solid rgba(74, 222, 128, 0.26);
  border-radius: 999px;
  background: rgba(14, 14, 14, 0.72);
  color: var(--green);
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  backdrop-filter: blur(10px);
}

.team-card-body {
  padding: 22px;
}

.team-card-modern .team-role {
  margin-bottom: 8px;
}

.team-card-modern .team-name {
  font-size: 1.65rem;
  line-height: 1;
  margin-bottom: 10px;
}

.team-desc {
  color: var(--text-dim);
  font-size: 0.83rem;
  line-height: 1.75;
  margin-bottom: 16px;
  font-weight: 300;
}

.team-card-modern .team-skills {
  justify-content: flex-start;
  margin-bottom: 0;
}

@media (max-width: 720px) {
  .team-section-head {
    display: block;
  }

  .team-section-head p {
    margin-top: 8px;
  }

  .team-grid-feature {
    grid-template-columns: 1fr;
  }
}
</style>
