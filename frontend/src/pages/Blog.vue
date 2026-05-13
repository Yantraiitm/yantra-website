<template>
  <div>
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Blog</span></div>
        <div class="live-badge"><div class="live-dot"></div>Live from Yantra Blogspot</div>
        <span class="tag">// Technical articles</span>
        <h1 class="page-hero-title">Blog</h1>
        <p class="page-hero-sub">Real write-ups, tutorials, and project breakdowns — fetched live from our Blogger.</p>
        <div class="blog-stats">
          <div class="bstat"><b>{{ statPosts }}</b><br>Total Posts</div>
          <div class="bstat"><b>{{ statCats }}</b><br>Categories</div>
          <div class="bstat"><b>Blogspot</b><br>Source</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">

        <div v-if="featuredPost" style="margin-bottom:10px;">
          <span class="tag">// Latest Post</span>
        </div>
        <a v-if="featuredPost" :href="featuredPost.url" target="_blank" rel="noopener" class="featured-post">
          <div class="featured-thumb">
            <img v-if="featuredPost.thumb" :src="featuredPost.thumb" :alt="featuredPost.title" @error="e => e.target.style.display='none'"/>
            <span v-else>{{ getCatEmoji(featuredPost.labels[0]) }}</span>
          </div>
          <div class="featured-body">
            <div class="featured-label">▶ Featured</div>
            <div style="margin-bottom:8px;">
              <span v-for="label in featuredPost.labels" :key="label" class="featured-label-badge">{{ getCatLabel(label) }}</span>
              <span v-if="!featuredPost.labels.length" class="featured-label-badge">Article</span>
            </div>
            <div class="featured-title">{{ featuredPost.title }}</div>
            <p class="featured-excerpt">{{ featuredPost.excerpt }}</p>
            <div class="featured-meta">
              <span>📅 {{ featuredPost.date }}</span>
              <span class="featured-meta-sep">|</span>
              <span>yantra-iitm.blogspot.com</span>
            </div>
            <div class="featured-btn">Read Full Article →</div>
          </div>
        </a>

        <div class="cat-tabs-wrap">
          <div class="cat-tabs">
            <template v-if="postsLoaded">
              <button
                v-for="tab in catTabList"
                :key="tab.key"
                class="cat-tab"
                :class="{ active: activeFilter === tab.key }"
                @click="activeFilter = tab.key"
              >
                {{ tab.emoji }} {{ tab.label }} <span class="cat-count">{{ tab.count }}</span>
              </button>
            </template>
            <template v-else>
              <div class="skel-line w60" style="height:34px; border-radius:100px; width:80px;"></div>
              <div class="skel-line w60" style="height:34px; border-radius:100px; width:110px;"></div>
              <div class="skel-line w60" style="height:34px; border-radius:100px; width:95px;"></div>
            </template>
          </div>
          <div class="results-info" v-if="postsLoaded">
            Showing <b>{{ visibleCount }}</b> post{{ visibleCount !== 1 ? 's' : '' }}
            <template v-if="activeFilter !== 'all'"> in this category</template>
          </div>
        </div>

        <div v-if="!postsLoaded && !fetchFailed" class="skel-grid">
          <div class="skel-card" v-for="i in 3" :key="i">
            <div class="skel-thumb"></div>
            <div class="skel-body">
              <div class="skel-line w60"></div>
              <div class="skel-line w90"></div>
              <div class="skel-line w75"></div>
            </div>
          </div>
        </div>

        <div v-if="fetchFailed && !postsLoaded" class="fetch-error">
          <div class="err-icon">⚠️</div>
          <h3>Could not load posts</h3>
          <p>Unable to reach the Yantra Blogspot feed right now.<br>Check your connection or <a href="https://yantra-iitm.blogspot.com/" target="_blank" style="color:var(--amber);">visit the blog directly</a>.</p>
        </div>

        <div v-if="postsLoaded" class="live-grid">
          <a
            v-for="(post, idx) in visiblePosts"
            :key="idx"
            :href="post.url"
            target="_blank"
            rel="noopener"
            class="b-card"
          >
            <div class="b-thumb">
              <img v-if="post.thumb" :src="post.thumb" :alt="post.title" loading="lazy" @error="e => e.target.style.display='none'"/>
              <div v-if="post.thumb" class="b-thumb-overlay"></div>
              <span v-if="!post.thumb" style="font-size:3rem;position:relative;z-index:1;">{{ getCatEmoji(post.labels[0]) }}</span>
            </div>
            <div class="b-body">
              <div class="b-cats">
                <span v-for="label in post.labels" :key="label" :class="'b-cat ' + getCatCls(label)">{{ getCatLabel(label) }}</span>
                <span v-if="!post.labels.length" class="b-cat cat-other">Article</span>
              </div>
              <div class="b-title">{{ post.title }}</div>
              <div class="b-excerpt">{{ post.excerpt }}</div>
              <div class="b-meta">
                <span class="b-date">📅 {{ post.date }}</span>
                <span class="b-link">Read →</span>
              </div>
            </div>
          </a>

          <div v-if="visibleCount === 0" class="empty-state">
            <div class="empty-icon">🔍</div>
            <p>No posts found in this category yet.</p>
          </div>
        </div>

        <div class="glow-line"></div>

        <div class="write-cta">
          <div style="font-size:2.2rem; margin-bottom:14px;">✍️</div>
          <h3>Write for Yantra</h3>
          <p>A Yantra member with a tutorial or project to share? Submit your article and get featured on our blog.</p>
          <a href="https://yantra-iitm.blogspot.com/" target="_blank" class="btn btn-primary" style="margin-right:10px;">Visit Blogspot →</a>
          <RouterLink to="/contact" class="btn btn-outline">Contact Us</RouterLink>
        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { RouterLink } from 'vue-router'

const BLOG_URL = 'https://yantra-iitm.blogspot.com'
const JSONP_CB = 'yantraFeedCB'

const allPosts = ref([])
const postsLoaded = ref(false)
const fetchFailed = ref(false)
const activeFilter = ref('all')
const statPosts = ref('—')
const statCats = ref('—')
const featuredPost = ref(null)

const CAT_CONFIG = {
  'arduino project': { label: 'Arduino', cls: 'cat-arduino', emoji: '⚡' },
  'drones': { label: 'Drones', cls: 'cat-drones', emoji: '🚁' },
  'rover': { label: 'Rover', cls: 'cat-rover', emoji: '🤖' },
  'getting started with physical bord': { label: 'Getting Started', cls: 'cat-getting', emoji: '🔧' },
  'getting started': { label: 'Getting Started', cls: 'cat-getting', emoji: '🔧' },
}
const CAT_EMOJI = { arduino: '⚡', drones: '🚁', rover: '🤖', getting: '🔧', other: '📝' }

function getCategoryKey(label) {
  const l = label.toLowerCase()
  if (l.includes('arduino')) return 'arduino'
  if (l.includes('drone')) return 'drones'
  if (l.includes('rover')) return 'rover'
  if (l.includes('getting') || l.includes('physical')) return 'getting'
  return 'other'
}

function getCatLabel(label) {
  const cfg = CAT_CONFIG[label.toLowerCase()]
  return cfg ? cfg.label : label
}

function getCatCls(label) {
  const key = getCategoryKey(label)
  return 'cat-' + key
}

function getCatEmoji(label) {
  if (!label) return '📝'
  const key = getCategoryKey(label)
  return CAT_EMOJI[key] || '📝'
}

function fmtDate(iso) {
  try { return new Date(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }) }
  catch { return iso.slice(0, 10) }
}

function stripHtml(html) {
  const d = document.createElement('div')
  d.innerHTML = html
  return d.textContent || d.innerText || ''
}

function makeExcerpt(html, len = 140) {
  const t = stripHtml(html).replace(/\s+/g, ' ').trim()
  return t.length > len ? t.slice(0, len).replace(/\s\S*$/, '') + '...' : t
}

function getThumb(entry) {
  if (entry.media$thumbnail) return entry.media$thumbnail.url.replace(/\/s[0-9]+-c\//, '/s600/')
  const content = entry.content?.$t || entry.summary?.$t || ''
  const m = content.match(/<img[^>]+src=["']([^"']+)["']/i)
  return m ? m[1] : null
}

function getPostUrl(entry) {
  const links = entry.link || []
  const alt = links.find(l => l.rel === 'alternate')
  return alt ? alt.href : BLOG_URL
}

const categoryCounts = computed(() => {
  const counts = {}
  allPosts.value.forEach(p => {
    const keys = p.labels.length ? [...new Set(p.labels.map(getCategoryKey))] : ['other']
    keys.forEach(k => { counts[k] = (counts[k] || 0) + 1 })
  })
  return counts
})

const catTabList = computed(() => {
  const tabs = [{ key: 'all', label: 'All', emoji: '', count: allPosts.value.length }]
  const cfg = { arduino: 'Arduino', drones: 'Drones', rover: 'Rover', getting: 'Getting Started', other: 'Other' }
  Object.entries(categoryCounts.value)
    .sort((a, b) => b[1] - a[1])
    .forEach(([key, count]) => {
      tabs.push({ key, label: cfg[key] || key, emoji: CAT_EMOJI[key] || '📂', count })
    })
  return tabs
})

const visiblePosts = computed(() => {
  if (activeFilter.value === 'all') return allPosts.value
  return allPosts.value.filter(p => {
    const keys = p.labels.length ? p.labels.map(getCategoryKey) : ['other']
    return keys.includes(activeFilter.value)
  })
})

const visibleCount = computed(() => visiblePosts.value.length)

let feedTimer = null

function processFeed(data) {
  try {
    clearTimeout(feedTimer)
    const entries = data.feed.entry || []
    if (!entries.length) throw new Error('No entries')

    const posts = entries.map(entry => ({
      title: entry.title.$t,
      url: getPostUrl(entry),
      date: fmtDate(entry.published.$t),
      excerpt: makeExcerpt(entry.content?.$t || entry.summary?.$t || ''),
      thumb: getThumb(entry),
      labels: (entry.category || []).map(c => c.term),
    }))

    allPosts.value = posts
    statPosts.value = posts.length + '+'
    statCats.value = Object.keys(categoryCounts.value).length
    featuredPost.value = posts[0] || null
    postsLoaded.value = true

    const s = document.getElementById('yantra-feed-script')
    if (s) s.remove()
  } catch (err) {
    showError()
  }
}

function showError() {
  clearTimeout(feedTimer)
  fetchFailed.value = true
  statPosts.value = '—'
  statCats.value = '—'
}

onMounted(() => {
  window[JSONP_CB] = processFeed

  const script = document.createElement('script')
  script.id = 'yantra-feed-script'
  script.src = `${BLOG_URL}/feeds/posts/default?alt=json-in-script&max-results=50&callback=${JSONP_CB}`
  script.onerror = showError
  feedTimer = setTimeout(() => { if (!postsLoaded.value) showError() }, 8000)
  document.head.appendChild(script)
})

onUnmounted(() => {
  clearTimeout(feedTimer)
  delete window[JSONP_CB]
  const s = document.getElementById('yantra-feed-script')
  if (s) s.remove()
})
</script>

<style scoped>
.live-badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: rgba(74,222,128,0.08);
  border: 1px solid rgba(74,222,128,0.22);
  border-radius: 100px;
  padding: 5px 13px 5px 8px;
  font-family: 'DM Mono', monospace;
  font-size: 0.62rem;
  color: #4ADE80;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 14px;
}
.live-dot {
  width: 6px; height: 6px;
  background: #4ADE80; border-radius: 50%;
  animation: blink 1.5s ease-in-out infinite;
  flex-shrink: 0;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.25} }

.blog-stats {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
  margin-top: 18px;
}
.bstat {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: var(--text-muted);
  letter-spacing: 0.08em;
}
.bstat b { color: var(--amber); font-size: 1rem; font-family: 'Bebas Neue', sans-serif; letter-spacing: 0.05em; font-weight: 400; }

.featured-post {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 0;
  background: var(--bg-card);
  border: 1px solid rgba(245,158,11,0.25);
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 52px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.4);
  transition: border-color 0.3s, box-shadow 0.3s;
  text-decoration: none;
  color: inherit;
}
.featured-post:hover { border-color: var(--amber); box-shadow: 0 12px 52px rgba(245,158,11,0.1); }
.featured-thumb {
  background: linear-gradient(135deg, rgba(245,158,11,0.14), rgba(234,88,12,0.06));
  display: flex; align-items: center; justify-content: center;
  font-size: 5rem;
  border-right: 1px solid var(--border);
  position: relative;
  overflow: hidden;
}
.featured-thumb img { width: 100%; height: 100%; object-fit: cover; position: absolute; inset: 0; }
.featured-body { padding: 32px; }
.featured-label {
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  color: #4ADE80;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.featured-label-badge {
  display: inline-block;
  padding: 2px 8px;
  background: rgba(245,158,11,0.1);
  border: 1px solid rgba(245,158,11,0.25);
  border-radius: 4px;
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  color: var(--amber);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 3px;
  margin-right: 5px;
}
.featured-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(1.4rem, 2.5vw, 2rem);
  letter-spacing: 0.04em;
  margin-bottom: 10px;
  line-height: 1.1;
}
.featured-excerpt {
  font-size: 0.88rem;
  color: var(--text-dim);
  line-height: 1.8;
  margin-bottom: 20px;
  font-weight: 300;
}
.featured-meta {
  display: flex; gap: 14px; align-items: center;
  font-family: 'DM Mono', monospace;
  font-size: 0.62rem;
  color: var(--text-muted);
  letter-spacing: 0.06em;
  margin-bottom: 20px;
}
.featured-meta-sep { opacity: 0.3; }
.featured-btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 10px 20px;
  background: var(--amber); color: #0E0E0E;
  border-radius: 5px;
  font-family: 'DM Mono', monospace;
  font-size: 0.68rem; font-weight: 600;
  letter-spacing: 0.08em; text-transform: uppercase;
  transition: background 0.25s;
}
.featured-btn:hover { background: #D97706; }

.cat-tabs-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: 32px;
}
.cat-tabs { display: flex; gap: 7px; flex-wrap: wrap; }
.cat-tab {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 8px 16px;
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 100px;
  font-family: 'DM Mono', monospace;
  font-size: 0.63rem;
  color: var(--text-muted);
  cursor: pointer;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transition: all 0.25s;
}
.cat-tab:hover { border-color: var(--amber); color: var(--amber); background: rgba(245,158,11,0.05); }
.cat-tab.active { border-color: var(--amber); color: var(--amber); background: rgba(245,158,11,0.1); }
.cat-count {
  background: rgba(245,158,11,0.15);
  color: var(--amber);
  border-radius: 100px;
  padding: 1px 6px;
  font-size: 0.58rem;
  min-width: 18px;
  text-align: center;
}
.cat-tab.active .cat-count { background: var(--amber); color: #0E0E0E; }
.results-info {
  font-family: 'DM Mono', monospace;
  font-size: 0.62rem;
  color: var(--text-muted);
  letter-spacing: 0.08em;
}
.results-info b { color: var(--amber); }

.live-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 52px;
}
.b-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.28s, border-color 0.28s, box-shadow 0.28s;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  text-decoration: none;
  color: inherit;
}
.b-card:hover { transform: translateY(-5px); border-color: var(--border-glow); box-shadow: 0 12px 40px rgba(0,0,0,0.5); }
.b-thumb {
  height: 160px;
  background: linear-gradient(135deg, rgba(245,158,11,0.1), rgba(234,88,12,0.04));
  display: flex; align-items: center; justify-content: center;
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}
.b-thumb img { width: 100%; height: 100%; object-fit: cover; position: absolute; inset: 0; transition: transform 0.4s ease; }
.b-card:hover .b-thumb img { transform: scale(1.05); }
.b-thumb-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 40%, var(--bg-card) 100%); }
.b-body { padding: 18px 20px 20px; flex: 1; display: flex; flex-direction: column; }
.b-cats { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 8px; }
.b-cat {
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  border: 1px solid;
}
.b-cat.cat-arduino { color: #60A5FA; background: rgba(96,165,250,0.08); border-color: rgba(96,165,250,0.22); }
.b-cat.cat-drones { color: #F59E0B; background: rgba(245,158,11,0.08); border-color: rgba(245,158,11,0.22); }
.b-cat.cat-rover { color: #4ADE80; background: rgba(74,222,128,0.08); border-color: rgba(74,222,128,0.22); }
.b-cat.cat-getting { color: #A78BFA; background: rgba(167,139,250,0.08); border-color: rgba(167,139,250,0.22); }
.b-cat.cat-other { color: var(--amber); background: rgba(245,158,11,0.08); border-color: rgba(245,158,11,0.18); }
.b-title { font-family: 'Bebas Neue', sans-serif; font-size: 1.15rem; letter-spacing: 0.04em; color: var(--text-primary); margin-bottom: 8px; line-height: 1.15; }
.b-excerpt { font-size: 0.8rem; color: var(--text-dim); line-height: 1.7; font-weight: 300; flex: 1; margin-bottom: 14px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.b-meta { display: flex; justify-content: space-between; align-items: center; margin-top: auto; }
.b-date { font-family: 'DM Mono', monospace; font-size: 0.6rem; color: var(--text-muted); letter-spacing: 0.07em; }
.b-link { font-family: 'DM Mono', monospace; font-size: 0.62rem; color: var(--amber); letter-spacing: 0.06em; }

.skel-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-bottom: 52px; }
.skel-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }
.skel-thumb { height: 160px; background: var(--muted); animation: shimmer 1.5s ease-in-out infinite; }
.skel-body { padding: 18px 20px; }
.skel-line { height: 10px; border-radius: 5px; background: var(--muted); animation: shimmer 1.5s ease-in-out infinite; margin-bottom: 10px; }
.skel-line.w60 { width: 60%; }
.skel-line.w90 { width: 90%; }
.skel-line.w75 { width: 75%; }
@keyframes shimmer { 0%,100%{opacity:0.4} 50%{opacity:0.8} }

.fetch-error { text-align: center; padding: 60px 20px; color: var(--text-muted); }
.err-icon { font-size: 3rem; margin-bottom: 14px; }
.fetch-error h3 { font-family: 'Bebas Neue', sans-serif; font-size: 1.4rem; letter-spacing: 0.06em; margin-bottom: 10px; color: var(--text-primary); }
.fetch-error p { font-size: 0.86rem; font-weight: 300; line-height: 1.7; }

.empty-state { grid-column: 1 / -1; text-align: center; padding: 48px 20px; }
.empty-icon { font-size: 2.5rem; margin-bottom: 12px; opacity: 0.5; }
.empty-state p { font-family: 'DM Mono', monospace; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.1em; }

.write-cta {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 44px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.write-cta::before {
  content: '';
  position: absolute;
  top: 0; left: 20%; right: 20%;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--amber), transparent);
}
.write-cta h3 { font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; letter-spacing: 0.06em; margin-bottom: 10px; }
.write-cta p { font-size: 0.88rem; color: var(--text-dim); max-width: 400px; margin: 0 auto 22px; line-height: 1.8; font-weight: 300; }

@media (max-width: 680px) {
  .featured-post { grid-template-columns: 1fr; }
  .featured-thumb { height: 180px; }
  .featured-body { padding: 22px; }
}
</style>
