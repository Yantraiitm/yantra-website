<template>
  <div>
    <section class="page-hero">
      <div class="container">
        <div class="breadcrumb">
          <RouterLink to="/">Home</RouterLink><span>/</span><span>Events</span>
        </div>
        <span class="tag">// Yantra calendar</span>
        <h1 class="page-hero-title">Events</h1>
        <p class="page-hero-sub">Workshops, talks, and build sessions from the Yantra Robotics Society.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="content-section-head">
          <span class="tag">// Event schedule</span>
          <h2 class="section-title reveal">Upcoming &amp; past events</h2>
        </div>
        <RoboticsLoader v-if="loading" label="Syncing event schedule" />
        <StatusBadge v-else-if="loadError" tone="error" :label="loadError" />
        <EmptyState v-else-if="!events.length" title="No events on the board"
          message="Check back soon for upcoming Yantra sessions." />
        <div v-if="!loading && !loadError && events.length" class="event-grid">
          <article v-for="event in events" :key="event.id" class="card event-card">
            <img v-if="event.image_url" :src="event.image_url" :alt="event.title">
            <div class="event-meta">{{ event.category || 'Event' }} · {{ formatDate(event.date) }}</div>
            <StatusBadge :tone="statusTone(event.registration_status)" :label="event.registration_status" />
            <h3>{{ event.title }}</h3>
            <p v-if="event.location">{{ event.location }}</p>
            <p>{{ event.description }}</p>
            <p v-if="event.max_attendees" class="capacity">{{ event.registered_attendees }} / {{ event.max_attendees }}
              registered</p>
            <a v-if="event.registration_url" class="btn btn-ghost" :href="event.registration_url" target="_blank"
              rel="noopener">More event information</a>
            <StatusBadge v-if="registrationForms[event.id].confirmation" tone="success"
              label="Registration confirmed" />
            <div v-if="registrationForms[event.id].confirmation" class="registration-confirmation">
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="m5 12 4 4L19 6" />
              </svg>
              <div><strong>{{ registrationForms[event.id].confirmation.title }}</strong><span>{{
                formatDate(registrationForms[event.id].confirmation.date) }}</span></div>
            </div>
            <form v-if="event.registration_status === 'open' && !registrationForms[event.id].confirmation"
              class="registration-form" @submit.prevent="registerForEvent(event)">
              <h4>Register for this event</h4>
              <input v-model="registrationForms[event.id].name" placeholder="Full name" autocomplete="name" required
                maxlength="150">
              <input v-model="registrationForms[event.id].email" type="email" placeholder="Email address"
                autocomplete="email" required maxlength="254">
              <input v-model="registrationForms[event.id].phone" type="tel" placeholder="Phone (optional)"
                autocomplete="tel" maxlength="32">
              <RoboticsLoader v-if="registrationForms[event.id].submitting" compact label="Registering attendee" />
              <button class="btn btn-amber" :disabled="registrationForms[event.id].submitting">{{
                registrationForms[event.id].submitting ? 'Registering…' : 'Register' }}</button>
              <StatusBadge v-if="registrationForms[event.id].message"
                :tone="registrationForms[event.id].isError ? 'error' : 'success'"
                :label="registrationForms[event.id].message" />
            </form>
          </article>
        </div>
        <div class="content-section-head insta-heading">
          <span class="tag">// Latest updates</span>
          <h2 class="section-title reveal">From Instagram</h2>
          <p class="section-subtitle">Updates and moments from the Yantra community.</p>
        </div>
        <div style="text-align:center;margin-bottom:28px"><a href="https://www.instagram.com/yantra_iitm/" target="_blank"
            rel="noopener" class="btn btn-amber">Explore @yantra_iitm on Instagram</a></div>
        <div class="reveal insta-feed">
          <RoboticsLoader v-if="instagramLoading" class="insta-loader" label="Loading Instagram feed" />
          <div class="elfsight-app-cae69c30-511d-4b2f-ac1f-8f7318cdd336"></div>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup>
import { onMounted, onUnmounted, reactive, ref } from 'vue'
import apiClient from '../services/api'
import { useScrollReveal } from '../composables/useScrollReveal'
import RoboticsLoader from '../components/RoboticsLoader.vue'
import StatusBadge from '../components/StatusBadge.vue'
import EmptyState from '../components/EmptyState.vue'
import { RouterLink } from 'vue-router'
useScrollReveal()
const events = ref([])
const loading = ref(true)
const loadError = ref('')
const instagramLoading = ref(true)
const registrationForms = reactive({})
let instagramTimer
const formatDate = (date) => new Date(date).toLocaleString(undefined, { dateStyle: 'medium', timeStyle: 'short' })
const statusTone = (status) => status === 'open' ? 'info' : (status === 'full' ? 'warning' : 'muted')
async function registerForEvent(event) {
  const form = registrationForms[event.id]
  form.submitting = true; form.message = ''; form.isError = false
  try {
    const { data } = await apiClient.post(`/events/${event.id}/registrations`, { name: form.name, email: form.email, phone: form.phone })
    form.message = data.message
    Object.assign(event, data.event)
    form.confirmation = { title: event.title, date: event.date }
    form.name = ''; form.email = ''; form.phone = ''
  } catch (error) {
    form.message = error.response?.data?.error || 'Registration could not be completed. Please try again.'; form.isError = true
    if (error.response?.data?.error === 'This event is full.') event.registration_status = 'full'
  } finally { form.submitting = false }
}
onMounted(() => {
  const existingScript = document.querySelector('script[src*="elfsight"]')
  if (existingScript) {
    instagramTimer = setTimeout(() => { instagramLoading.value = false }, 2500)
  } else {
    const script = document.createElement('script'); script.src = 'https://static.elfsight.com/platform/platform.js'; script.async = true
    script.addEventListener('load', () => { clearTimeout(instagramTimer); instagramTimer = setTimeout(() => { instagramLoading.value = false }, 1200) }, { once: true })
    script.addEventListener('error', () => { clearTimeout(instagramTimer); instagramLoading.value = false }, { once: true })
    document.head.appendChild(script)
    instagramTimer = setTimeout(() => { instagramLoading.value = false }, 9000)
  }
  apiClient.get('/events').then(({ data }) => {
    events.value = data
    data.forEach((event) => { registrationForms[event.id] = { name: '', email: '', phone: '', submitting: false, message: '', isError: false, confirmation: null } })
  }).catch((error) => { loadError.value = error.response?.data?.error || 'Events could not be loaded. Please refresh the page.' }).finally(() => { loading.value = false })
})
onUnmounted(() => clearTimeout(instagramTimer))
</script>
<style scoped>
.event-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  align-items: start;
}

.event-card {
  height: 470px;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--accent-cyan) rgba(148,163,184,.12);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 7px;
  padding: 16px;
  border-color: rgba(34,211,238,.2);
  background: linear-gradient(155deg,rgba(34,211,238,.055),transparent 38%),var(--bg-card);
}
.event-card::-webkit-scrollbar { width: 6px; }
.event-card::-webkit-scrollbar-thumb { background: rgba(34,211,238,.42); border-radius: 9px; }
.event-card::-webkit-scrollbar-track { background: rgba(148,163,184,.08); }

.event-card img {
  width: 100%;
  height: 150px;
  flex: 0 0 150px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 4px
}

.event-card h3 {
  margin: 3px 0;
  line-height: 1.25
}

.event-card p {
  color: var(--text-dim);
  margin: 0 0 5px;
  line-height: 1.45
}
.event-card .registration-form { width:100%; margin-top:auto; }
.insta-heading { margin-top:78px; }
.insta-feed { position:relative; min-height:220px; padding:18px; border:1px solid var(--border); border-radius:16px; background:rgba(15,23,42,.42); }
.insta-loader { position:absolute; inset:0; z-index:2; display:grid; place-items:center; background:rgba(7,11,19,.92); border-radius:inherit; }

.event-meta {
  color: var(--amber);
  font-family: 'Share Tech Mono', monospace;
  font-size: .76rem
}

.event-status {
  display: inline-block;
  width: max-content;
  margin-top: 10px;
  padding: 4px 9px;
  border-radius: 99px;
  text-transform: uppercase;
  font: .68rem 'Share Tech Mono', monospace
}

.status-open {
  color: #4ade80;
  background: rgba(74, 222, 128, .1)
}

.status-full,
.status-past {
  color: #f87171;
  background: rgba(248, 113, 113, .1)
}

.capacity {
  font-size: .85rem
}

.registration-form {
  display: grid;
  gap: 7px;
  margin-top: 8px;
  padding-top: 10px;
  border-top: 1px solid var(--border)
}

.registration-form input {
  width: 100%;
  padding: 8px 10px;
  color: var(--text);
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px
}

.event-feedback {
  margin: 10px 0;
  color: var(--text-dim)
}

.event-feedback.error {
  color: #fb7185
}
@media(max-width:640px){.event-card{height:450px}.insta-heading{margin-top:56px}}
</style>
