<template>
  <div>
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Courses</span></div>
        <span class="tag">// Learn with us</span>
        <h1 class="page-hero-title">Learning Modules</h1>
        <p class="page-hero-sub">Structured learning paths from beginner to advanced in robotics and embedded engineering.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">

        <div class="reveal" style="background:linear-gradient(135deg,rgba(59,130,246,0.1),rgba(6,182,212,0.05)); border:1px solid rgba(59,130,246,0.2); border-radius:12px; padding:32px 36px; display:flex; align-items:center; gap:24px; margin-bottom:64px; flex-wrap:wrap;">
          <div style="width:48px;height:48px;color:var(--amber);flex-shrink:0;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg></div>
          <div>
            <div style="font-family:'Orbitron',sans-serif; font-size:1rem; font-weight:700; margin-bottom:6px; color:var(--accent-cyan);">Recommended Learning Path</div>
            <p style="color:var(--text-dim); font-size:0.9rem;">
              Start with <strong style="color:var(--text-primary);">Intro to Robotics</strong> → move to
              <strong style="color:var(--text-primary);">Embedded Systems</strong> → then dive into
              <strong style="color:var(--text-primary);">Computer Vision</strong> or
              <strong style="color:var(--text-primary);">AI &amp; ML</strong> depending on your interest.
            </p>
          </div>
        </div>

        <span class="tag">// YouTube Courses</span>
        <h2 class="section-title reveal">Video Tutorials</h2>
        <p class="section-subtitle reveal" style="text-align:center; color:var(--text-muted); margin-bottom:40px; max-width:600px; margin-left:auto; margin-right:auto;">
          Free video courses from our YouTube channel. Learn at your own pace with hands-on tutorials.
        </p>

        <div class="youtube-grid" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(350px, 1fr)); gap:24px; margin-bottom:64px;">
          <div
            v-for="(playlist, index) in YOUTUBE_PLAYLISTS"
            :key="index"
            class="course-card reveal yt-playlist-card"
            :style="{ animationDelay: index * 0.1 + 's' }"
          >
            <div class="course-thumbnail">
              <img
                :src="generateThumbnailUrl(playlist.url)"
                :alt="playlist.title"
                loading="lazy"
                @error="e => e.target.src = fallbackThumb"
              >
              <div class="play-button">▶</div>
              <a :href="convertToPlaylistUrl(playlist.url)" target="_blank" rel="noopener noreferrer" class="playlist-link" title="Watch on YouTube"></a>
            </div>
            <div class="course-body">
              <div class="course-header">
                <h3 class="course-title">{{ playlist.title }}</h3>
                <span class="course-level" :style="getLevelStyle(playlist.level)">{{ playlist.level }}</span>
              </div>
              <p class="course-instructor"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:13px;height:13px;display:inline;vertical-align:middle;margin-right:4px;"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg> Instructor: <strong>{{ playlist.instructor }}</strong></p>
              <p class="course-desc">{{ playlist.description }}</p>
              <div class="course-tags">
                <span v-for="tag in playlist.tags" :key="tag" class="tech-tag">{{ tag }}</span>
              </div>
              <div class="course-meta">
                <span class="course-videos"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:13px;height:13px;display:inline;vertical-align:middle;margin-right:3px;"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg> {{ playlist.videoCount > 0 ? playlist.videoCount + ' videos' : 'View Playlist' }}</span>
                <span class="course-platform">YouTube</span>
              </div>
              <a :href="convertToPlaylistUrl(playlist.url)" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top:16px; width:100%; text-align:center; display:block;">
                Watch Playlist →
              </a>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-bottom:64px;" class="reveal">
          <a href="https://www.youtube.com/@yantraiitmbs" target="_blank" class="btn btn-youtube">
            Subscribe to Our YouTube Channel →
          </a>
        </div>

        <span class="tag">// Level 01 — Beginner</span>
        <h2 class="section-title reveal">Foundation Courses</h2>
        <div class="foundation-courses-grid">

          <div class="course-card reveal">
            <div class="course-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M12 11V7M8 7h8M7 15h.01M17 15h.01"/><circle cx="12" cy="4" r="2"/></svg></div>
            <div class="course-body">
              <div class="course-header">
                <h3 class="course-title">Introduction to Robotics</h3>
                <span class="course-level beginner">Beginner</span>
              </div>
              <p class="course-desc">Build your foundation in robot mechanics, control, and programming.</p>
              <ul class="course-modules">
                <li>Basics of Robotics</li>
                <li>Sensors &amp; Actuators</li>
                <li>Control Systems</li>
                <li>Robot Programming</li>
                <li>Project: Line Follower</li>
              </ul>
              <div class="course-meta">
                <span class="tech-tag">Beginner</span>
                <span class="course-duration">~8 hrs</span>
              </div>
            </div>
          </div>

          <div class="course-card reveal">
            <div class="course-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6v6H9z"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M18 9h3M3 15h3M18 15h3"/></svg></div>
            <div class="course-body">
              <div class="course-header">
                <h3 class="course-title">Embedded Systems Basics</h3>
                <span class="course-level beginner">Beginner</span>
              </div>
              <p class="course-desc">Get started with microcontrollers and hardware programming.</p>
              <ul class="course-modules">
                <li>Microcontrollers 101</li>
                <li>GPIO &amp; Digital I/O</li>
                <li>Interrupts &amp; Timers</li>
                <li>Serial Communication</li>
                <li>Project: LED Matrix</li>
              </ul>
              <div class="course-meta">
                <span class="tech-tag">Beginner</span>
                <span class="course-duration">~10 hrs</span>
              </div>
            </div>
          </div>

          <div class="course-card reveal">
            <div class="course-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div>
            <div class="course-body">
              <div class="course-header">
                <h3 class="course-title">Python for Robotics</h3>
                <span class="course-level beginner">Beginner</span>
              </div>
              <p class="course-desc">Python fundamentals tailored for robotics and automation tasks.</p>
              <ul class="course-modules">
                <li>Python Basics</li>
                <li>NumPy &amp; Arrays</li>
                <li>Serial &amp; GPIO Libs</li>
                <li>Data Visualization</li>
                <li>Project: Sensor Logger</li>
              </ul>
              <div class="course-meta">
                <span class="tech-tag">Beginner</span>
                <span class="course-duration">~6 hrs</span>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal'

useScrollReveal()

const YOUTUBE_PLAYLISTS = [
  {
    title: 'Summer Camp - IoT Fundamentals',
    instructor: 'Abhinav',
    description: 'Learn the basics of IoT, sensors, and actuators. Perfect starting point for beginners interested in robotics and embedded systems.',
    url: 'https://www.youtube.com/watch?v=MXULHiQH_94&list=PLxmVtBfIwPgPJkU8U4ek45RAWCZB246PJ',
    videoCount: 2,
    level: 'Beginner',
    tags: ['IoT', 'Sensors', 'Beginner']
  },
  {
    title: 'Robot Building with ESP32/ESP8266',
    instructor: 'Akhilesh',
    description: 'Build your first robot from scratch using ESP32/ESP8266 microcontrollers. Learn programming, circuit design, and motor control.',
    url: 'https://www.youtube.com/watch?v=bQRRDlNTNBQ&list=PLxmVtBfIwPgOzdLVBn2c_AuPQ4XD2JOAn',
    videoCount: 5,
    level: 'Beginner',
    tags: ['ESP32', 'Robotics', 'Beginner']
  },
  {
    title: 'Robot Building with C Programming',
    instructor: 'Akhilesh',
    description: 'Complete summary of robot building with fundamentals of C programming for embedded systems and microcontroller development.',
    url: 'https://www.youtube.com/watch?v=5dZFVPtd7Lc&list=PLxmVtBfIwPgPShDsEay1gOGrxSiMNa_qw',
    videoCount: 12,
    level: 'Intermediate',
    tags: ['C Programming', 'Embedded', 'Intermediate']
  },
  {
    title: 'Drone Building Masterclass',
    instructor: 'Vivek',
    description: 'Complete drone building course from basic to advanced. Learn aerodynamics, flight controllers, and autonomous navigation.',
    url: 'https://www.youtube.com/watch?v=5V0DgCnyuWk&list=PLxmVtBfIwPgPGhIX0rCIfc4AH4oFbUBT-',
    videoCount: 3,
    level: 'Intermediate',
    tags: ['Drones', 'Flight Control', 'Intermediate']
  },
  {
    title: 'Robotic Arm Design & Control',
    instructor: 'Arunya',
    description: 'Build a functional robotic arm from scrap materials. Learn kinematics, servo control, and task automation.',
    url: 'https://www.youtube.com/watch?v=_GaL_6PKlyM&list=PLxmVtBfIwPgPICljmSZ6i6Sc_KjgOtiy2',
    videoCount: 2,
    level: 'Advanced',
    tags: ['Robotic Arm', 'Kinematics', 'Advanced']
  },
  {
    title: 'AI Interactive Bot Development',
    instructor: 'Arunya',
    description: 'Build Your Own AI Interactive Bot - Complete session series covering AI integration, natural language processing, and interactive systems.',
    url: 'https://www.youtube.com/watch?v=9BH4hMDau7w&list=PLxmVtBfIwPgO-sAp7gGmpnUkoMGjVSd83',
    videoCount: 3,
    level: 'Advanced',
    tags: ['AI', 'Machine Learning', 'Advanced']
  }
]

const fallbackThumb = 'data:image/svg+xml,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 225"><rect fill="#1e293b" width="400" height="225"/><text fill="#06b6d4" font-family="sans-serif" font-size="60" x="50%" y="50%" text-anchor="middle" dy=".3em">▶</text></svg>')

function extractVideoId(url) {
  if (!url) return null
  const watchMatch = url.match(/[?&]v=([^&]+)/)
  if (watchMatch) return watchMatch[1]
  const embedMatch = url.match(/\/embed\/([^?&]+)/)
  if (embedMatch) return embedMatch[1]
  const shortMatch = url.match(/youtu\.be\/([^?&]+)/)
  if (shortMatch) return shortMatch[1]
  return null
}

function extractPlaylistId(url) {
  if (!url) return null
  const listMatch = url.match(/[?&]list=([^&]+)/)
  return listMatch ? listMatch[1] : null
}

function generateThumbnailUrl(url) {
  const videoId = extractVideoId(url)
  if (videoId) return `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`
  return fallbackThumb
}

function convertToPlaylistUrl(url) {
  const playlistId = extractPlaylistId(url)
  return playlistId ? `https://www.youtube.com/playlist?list=${playlistId}` : url
}

function getLevelStyle(level) {
  switch (level) {
    case 'Beginner':    return 'background:rgba(34,197,94,0.1);border-color:rgba(34,197,94,0.3);color:#22c55e;'
    case 'Intermediate': return 'background:rgba(234,179,8,0.1);border-color:rgba(234,179,8,0.3);color:#eab308;'
    case 'Advanced':    return 'background:rgba(239,68,68,0.1);border-color:rgba(239,68,68,0.3);color:#ef4444;'
    default:            return 'background:rgba(59,130,246,0.1);border-color:rgba(59,130,246,0.3);color:#3b82f6;'
  }
}
</script>

<style scoped>
.foundation-courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  margin-bottom: 64px;
}
.playlist-link {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 10;
}
.course-instructor {
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 12px;
}
.course-instructor strong { color: var(--accent-cyan); }
.course-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 15px;
}
.course-videos {
  font-size: 13px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 5px;
}
.btn-youtube {
  background: #FF0000 !important;
  color: white !important;
  border: none !important;
  padding: 15px 35px !important;
  border-radius: 8px !important;
  font-weight: 600 !important;
  transition: all 0.3s ease !important;
  text-decoration: none;
  display: inline-block;
}
.btn-youtube:hover {
  background: #cc0000 !important;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(255, 0, 0, 0.3);
}
</style>
