<template>
  <div>
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Projects</span></div>
        <span class="tag">// What we build</span>
        <h1 class="page-hero-title">Projects</h1>
        <p class="page-hero-sub">From laser battle robots to autonomous navigation — real systems built by Yantra.</p>
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
            @click="setFilter(tab.value)"
          >{{ tab.label }}</button>
        </div>

        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Fetching projects from GitHub...</p>
        </div>

        <div v-if="error && !loading" class="error-state">
          <p v-if="rateLimited">GitHub API rate limit reached. Wait a few minutes and refresh.</p>
          <p v-else>Unable to load projects. Please try again later.</p>
          <p style="margin-top:8px; font-size:0.8rem; color:var(--text-muted);">
            <a href="https://github.com/Yantraiitm" target="_blank" style="color:var(--amber);">Browse on GitHub →</a>
          </p>
        </div>

        <div v-if="!loading" class="projects-grid">
          <div
            v-for="repo in filteredRepos"
            :key="repo.id"
            class="project-card"
          >
            <div class="project-img project-img-icon" v-html="getFallbackIcon(detectCategory(repo))"></div>
            <div class="project-body">
              <div class="project-header">
                <h3 class="project-title">{{ repo.name }}</h3>
                <a :href="repo.html_url" target="_blank" class="github-link" title="View on GitHub">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                  </svg>
                </a>
              </div>
              <p class="project-desc">{{ repo.description || 'No description available. Click to view on GitHub.' }}</p>
              <div class="project-tags">
                <span class="tech-tag">{{ repo.language || 'Code' }}</span>
                <span v-for="topic in (repo.topics || []).slice(0, 3)" :key="topic" class="tech-tag">{{ topic }}</span>
              </div>
              <div class="project-stats">
                <span class="stat"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:12px;height:12px;display:inline;vertical-align:middle;margin-right:3px;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>{{ repo.stargazers_count }}</span>
                <span class="stat"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:12px;height:12px;display:inline;vertical-align:middle;margin-right:3px;"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M6 9v6M15.4 6A9 9 0 009 15.4"/></svg>{{ repo.forks_count }}</span>
                <span class="stat"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:12px;height:12px;display:inline;vertical-align:middle;margin-right:3px;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{{ formatDate(repo.updated_at) }}</span>
              </div>
              <a :href="repo.html_url" target="_blank" class="btn btn-ghost" style="margin-top:16px; font-size:0.7rem; padding:8px 18px;">
                View Repository →
              </a>
            </div>
          </div>

          <p v-if="!loading && !error && filteredRepos.length === 0 && repos.length > 0" style="text-align:center;color:var(--text-dim);padding:40px;">
            No projects found in this category.
          </p>
        </div>

        <div class="glow-line"></div>
        <div class="reveal" style="background:var(--bg-card); border:1px solid var(--border); border-radius:12px; padding:40px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:24px;">
          <div>
            <h3 style="font-family:'Orbitron',sans-serif; font-size:1.1rem; font-weight:700; margin-bottom:8px;">Have a project idea?</h3>
            <p style="color:var(--text-dim); font-size:0.9rem;">Pitch your robotics project and work with Yantra to bring it to life.</p>
          </div>
          <a href="mailto:yantra@study.iitm.ac.in" class="btn btn-primary">Propose a Project ↗</a>
        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useScrollReveal } from '../composables/useScrollReveal'

useScrollReveal()

const repos = ref([])
const loading = ref(true)
const error = ref(false)
const activeFilter = ref('all')

const tabs = [
  { value: 'all', label: 'All' },
  { value: 'robotics', label: 'Robotics' },
  { value: 'embedded', label: 'Embedded' },
  { value: 'ai', label: 'AI / ML' },
  { value: 'vision', label: 'Computer Vision' },
  { value: 'iot', label: 'IoT' },
]

const GITHUB_USERS = ['Ester-D-Kate', 'Okami-423', 'akhileshkrbhagat1']

const EXTRA_REPOS = [
  {
    id: -101,
    name: 'Predominant-Music',
    html_url: 'https://github.com/cscprojishnu/Predominant-Music',
    description: 'AI-powered music genre detection using audio feature extraction and machine learning models.',
    language: 'Python',
    topics: ['ai', 'ml', 'audio'],
    stargazers_count: 0,
    forks_count: 0,
    updated_at: new Date().toISOString(),
  },
  {
    id: -102,
    name: 'Solar-Safe-Edge-AI-Powered-Fault-Detection-in-Photovoltaic-Modules-using-AI-ML',
    html_url: 'https://github.com/cscprojishnu/Solar-Safe-Edge-AI-Powered-Fault-Detection-in-Photovoltaic-Modules-using-AI-ML',
    description: 'Edge AI fault detection for photovoltaic modules that uses ML to monitor solar panel health and detect failures.',
    language: 'Python',
    topics: ['ai', 'ml', 'edge-ai', 'solar'],
    stargazers_count: 0,
    forks_count: 0,
    updated_at: new Date().toISOString(),
  },
  {
    id: -103,
    name: 'ADMM-for-Sparse-Deep-Neural-Network-Pruning-USING-CNN-INN',
    html_url: 'https://github.com/cscprojishnu/ADMM-for-Sparse-Deep-Neural-Network-Pruning-USING-CNN-INN',
    description: 'ADMM-based sparse pruning for CNNs to reduce neural network size while preserving model accuracy.',
    language: 'Python',
    topics: ['ai', 'ml', 'deep-learning', 'pruning'],
    stargazers_count: 0,
    forks_count: 0,
    updated_at: new Date().toISOString(),
  },
]

const CATEGORY_KEYWORDS = {
  robotics: ['robot', 'rover', 'arm', 'drone', 'autonomous', 'navigation', 'slam'],
  embedded: ['embedded', 'esp32', 'arduino', 'stm32', 'microcontroller', 'pcb', 'firmware'],
  ai: ['ai', 'ml', 'machine-learning', 'deep-learning', 'neural', 'pytorch', 'tensorflow'],
  vision: ['vision', 'opencv', 'image', 'detection', 'yolo', 'camera', 'tracking'],
  iot: ['iot', 'mqtt', 'sensor', 'wireless', 'cloud', 'dashboard', 'telemetry'],
}

const FALLBACK_ICONS = {
  robotics: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:48px;height:48px;color:#F59E0B"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M12 11V7M8 7h8M7 15h.01M17 15h.01"/><circle cx="12" cy="4" r="2"/></svg>',
  embedded: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:48px;height:48px;color:#F59E0B"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6v6H9z"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M18 9h3M3 15h3M18 15h3"/></svg>',
  ai: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:48px;height:48px;color:#F59E0B"><circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M12 7v4M12 11l-5 6M12 11l5 6"/></svg>',
  vision: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:48px;height:48px;color:#F59E0B"><ellipse cx="12" cy="12" rx="10" ry="6"/><circle cx="12" cy="12" r="3"/></svg>',
  iot: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:48px;height:48px;color:#F59E0B"><path d="M5 12.55a11 11 0 0114.08 0"/><path d="M1.42 9a16 16 0 0121.16 0"/><path d="M8.53 16.11a6 6 0 016.95 0"/><circle cx="12" cy="20" r="1" fill="currentColor"/></svg>',
  default: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="width:48px;height:48px;color:#F59E0B"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
}

function detectCategory(repo) {
  const topics = repo.topics || []
  const name = repo.name.toLowerCase()
  const desc = (repo.description || '').toLowerCase()
  const lang = (repo.language || '').toLowerCase()

  for (const [cat, kws] of Object.entries(CATEGORY_KEYWORDS)) {
    if (topics.some(t => kws.some(k => t.toLowerCase().includes(k)))) return cat
  }
  const text = `${name} ${desc} ${lang}`
  for (const [cat, kws] of Object.entries(CATEGORY_KEYWORDS)) {
    if (kws.some(k => text.includes(k))) return cat
  }
  if (lang === 'python') return 'ai'
  if (lang === 'c' || lang === 'c++') return 'embedded'
  if (lang === 'javascript') return 'iot'
  return 'robotics'
}

function getFallbackIcon(cat) {
  return FALLBACK_ICONS[cat] || FALLBACK_ICONS.default
}

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
}

const filteredRepos = computed(() => {
  if (activeFilter.value === 'all') return repos.value
  return repos.value.filter(r => detectCategory(r) === activeFilter.value)
})

function setFilter(val) {
  activeFilter.value = val
}

const rateLimited = ref(false)
const CACHE_KEY = 'yantra_gh_repos'
const CACHE_TTL = 5 * 60 * 1000 // 5 minutes

async function fetchJSON(url) {
  const res = await fetch(url)
  if (res.status === 403 || res.status === 429) { rateLimited.value = true; return null }
  if (!res.ok) return null
  return res.json()
}

onMounted(async () => {
  // Serve from cache if fresh
  try {
    const cached = localStorage.getItem(CACHE_KEY)
    if (cached) {
      const { ts, data } = JSON.parse(cached)
      if (Date.now() - ts < CACHE_TTL && data.length > 0) {
        repos.value = data
        loading.value = false
        return
      }
    }
  } catch {}

  try {
    const all = []
    for (const user of GITHUB_USERS) {
      const data = await fetchJSON(`https://api.github.com/users/${user}/repos?sort=updated&per_page=10`)
      if (data) data.forEach(r => { r.owner_username = user; all.push(r) })
    }

    // Deduplicate by repo id and merge with explicit AI/ML projects
    const seen = new Set()
    const fetched = all.filter(r => { if (seen.has(r.id)) return false; seen.add(r.id); return true })
    repos.value = [...EXTRA_REPOS, ...fetched]

    if (repos.value.length === EXTRA_REPOS.length) error.value = true
    else {
      try { localStorage.setItem(CACHE_KEY, JSON.stringify({ ts: Date.now(), data: repos.value })) } catch {}
    }
  } catch {
    error.value = true
    repos.value = [...EXTRA_REPOS]
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 60px 0;
  color: var(--text-dim);
}
.spinner {
  width: 36px; height: 36px;
  border: 3px solid var(--border);
  border-top-color: var(--amber);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.error-state {
  text-align: center;
  padding: 60px 20px;
  color: var(--text-muted);
}
</style>
