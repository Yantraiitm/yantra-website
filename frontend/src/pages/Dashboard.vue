<template>
  <div>
    <section class="page-hero dashboard-hero">
      <div class="container">
        <div class="breadcrumb"><RouterLink to="/">Home</RouterLink><span>/</span><span>Dashboard</span></div>
        <span class="tag">// Logged in</span>
        <h1 class="page-hero-title">Welcome back, {{ user?.name }}</h1>
        <p class="page-hero-sub">Access your member dashboard, view protected sections, and continue building with Yantra.</p>
      </div>
    </section>

    <section class="section">
      <div class="container dashboard-grid">
        <article class="dashboard-card">
          <h3>Member profile</h3>
          <p>Email: {{ user?.email }}</p>
          <p>Roles: {{ user?.roles?.join(', ') || 'Member' }}</p>
        </article>

        <article class="dashboard-card">
          <h3>Quick links</h3>
          <ul>
            <li><RouterLink to="/projects">Projects</RouterLink></li>
            <li><RouterLink to="/events">Events</RouterLink></li>
            <li><RouterLink to="/team">Team</RouterLink></li>
          </ul>
        </article>
      </div>
    </section>

    <section v-if="userStore.isAdmin" class="section">
      <div class="container">
        <span class="tag">// Content management</span>
        <h2 class="section-title">Manage team, images &amp; events</h2>
        <div class="dashboard-grid editor-panels">
          <details ref="memberPanel" class="admin-form-panel">
            <summary>Team profile editor <span>Add or update a team member</span></summary>
          <form ref="memberEditor" class="dashboard-card editor" @submit.prevent="saveMember">
            <h3>{{ memberForm.id ? 'Edit team member' : 'Add team member' }}</h3>
            <input v-model="memberForm.name" placeholder="Name" required>
            <input v-model="memberForm.role" placeholder="Role / designation" required>
            <textarea v-model="memberForm.description" placeholder="Short description" />
            <input v-model="memberForm.skills" placeholder="Skills, comma separated">
            <label>Profile image (JPG or PNG)<input type="file" accept="image/jpeg,image/png,.jpg,.jpeg,.png" @change="uploadImage($event, memberForm)"></label>
            <StatusBadge v-if="uploadStatus.member" :tone="isUploading('member') ? 'info' : 'success'" :label="uploadStatus.member" />
            <progress v-if="isUploading('member')" :value="uploadProgress.member" max="100"></progress>
            <img v-if="memberForm.image_url" class="image-preview" :src="memberForm.image_url" alt="Selected profile preview">
            <button class="btn btn-amber" :disabled="isUploading('member')">{{ memberForm.id ? 'Save member' : 'Add member' }}</button>
          </form>
          </details>
          <details class="admin-form-panel">
            <summary>Gallery image editor <span>Add a collection image</span></summary>
          <form class="dashboard-card editor" @submit.prevent="saveImage">
            <h3>Add gallery image</h3>
            <label>Image file (JPG or PNG)<input type="file" accept="image/jpeg,image/png,.jpg,.jpeg,.png" required @change="uploadImage($event, imageForm)"></label>
            <StatusBadge v-if="uploadStatus.gallery" :tone="isUploading('gallery') ? 'info' : 'success'" :label="uploadStatus.gallery" />
            <progress v-if="isUploading('gallery')" :value="uploadProgress.gallery" max="100"></progress>
            <img v-if="imageForm.image_url" class="image-preview" :src="imageForm.image_url" alt="Selected gallery preview">
            <input v-model="imageForm.caption" placeholder="Caption">
            <input v-model="imageForm.category" placeholder="Category (workshops, team…)" >
            <button class="btn btn-amber" :disabled="isUploading('gallery')">Add image</button>
          </form>
          </details>
          <details ref="eventPanel" class="admin-form-panel">
            <summary>Event editor <span>Create events and set attendee limits</span></summary>
          <form class="dashboard-card editor" @submit.prevent="saveEvent">
            <h3>{{ eventForm.id ? 'Edit event' : 'Add event' }}</h3>
            <input v-model="eventForm.title" placeholder="Title" required>
            <input v-model="eventForm.date" type="datetime-local" required>
            <input v-model="eventForm.category" placeholder="Category">
            <input v-model="eventForm.location" placeholder="Location">
            <input v-model.number="eventForm.max_attendees" type="number" min="1" placeholder="Attendee limit (optional)">
            <textarea v-model="eventForm.description" placeholder="Description" />
            <label>Event image (JPG or PNG)<input type="file" accept="image/jpeg,image/png,.jpg,.jpeg,.png" @change="uploadImage($event, eventForm)"></label>
            <StatusBadge v-if="uploadStatus.event" :tone="isUploading('event') ? 'info' : 'success'" :label="uploadStatus.event" />
            <progress v-if="isUploading('event')" :value="uploadProgress.event" max="100"></progress>
            <img v-if="eventForm.image_url" class="image-preview" :src="eventForm.image_url" alt="Selected event preview">
            <input v-model="eventForm.registration_url" placeholder="Registration URL (optional)">
            <button class="btn btn-amber" :disabled="isUploading('event')">{{ eventForm.id ? 'Save event' : 'Add event' }}</button>
          </form>
          </details>
        </div>
        <StatusBadge v-if="message" :tone="isError ? 'error' : 'success'" :label="message" />
        <div class="dashboard-grid managed-content" style="margin-top:24px">
          <RoboticsLoader v-if="contentLoading" label="Syncing admin console" />
          <template v-else>
          <article class="dashboard-card"><h3>Team members</h3><EmptyState v-if="!members.length" title="Roster is empty" message="Add the first team profile using the editor above." /><p v-for="(item, index) in members" :key="item.id" class="managed-row">{{ item.name }} <span class="row-actions"><button class="icon-action" type="button" aria-label="Move up" title="Move up" :disabled="index === 0" @click="reorder(members, index, -1, '/team')">↑</button><button class="icon-action" type="button" aria-label="Move down" title="Move down" :disabled="index === members.length - 1" @click="reorder(members, index, 1, '/team')">↓</button><button class="icon-action" type="button" :aria-label="`Edit ${item.name}`" title="Edit" @click="editMember(item)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4Z"/></svg></button><button class="icon-action delete-action" type="button" :aria-label="`Delete ${item.name}`" title="Delete" @click="remove('/team', item.id, members)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M8 6V4h8v2m3 0-1 14H6L5 6m4 4v6m6-6v6"/></svg></button></span></p></article>
          <article class="dashboard-card"><h3>Gallery images</h3><EmptyState v-if="!images.length" title="No gallery uploads" message="Add a JPG or PNG image with the editor above." /><p v-for="(item, index) in images" :key="item.id" class="managed-row">{{ item.caption || item.image_url }} <span class="row-actions"><button class="icon-action" type="button" aria-label="Move up" title="Move up" :disabled="index === 0" @click="reorder(images, index, -1, '/gallery')">↑</button><button class="icon-action" type="button" aria-label="Move down" title="Move down" :disabled="index === images.length - 1" @click="reorder(images, index, 1, '/gallery')">↓</button><button class="icon-action delete-action" type="button" :aria-label="`Delete ${item.caption || 'image'}`" title="Delete image" @click="remove('/gallery', item.id, images)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M8 6V4h8v2m3 0-1 14H6L5 6m4 4v6m6-6v6"/></svg></button></span></p></article>
          <article class="dashboard-card"><h3>Events</h3><EmptyState v-if="!events.length" title="No events scheduled" message="Create an event above to open registration." /><div v-for="item in events" :key="item.id" class="event-admin-row"><p class="managed-row">{{ item.title }} <span class="row-actions"><button class="icon-action" type="button" :aria-label="`Edit ${item.title}`" title="Edit" @click="editEvent(item)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4Z"/></svg></button><button class="icon-action delete-action" type="button" :aria-label="`Delete ${item.title}`" title="Delete" @click="remove('/events', item.id, events)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M8 6V4h8v2m3 0-1 14H6L5 6m4 4v6m6-6v6"/></svg></button></span></p><details class="attendee-list"><summary>Attendees ({{ item.registered_attendees || 0 }})</summary><button v-if="!attendeesLoaded[item.id]" class="btn btn-ghost" type="button" @click="loadAttendees(item.id)">Load attendee list</button><RoboticsLoader v-if="attendeeLoading[item.id]" compact label="Loading attendees" /><p v-for="attendee in (attendees[item.id] || [])" :key="attendee.id">{{ attendee.name }} · {{ attendee.email }} <span v-if="attendee.phone">· {{ attendee.phone }}</span></p><EmptyState v-if="attendeesLoaded[item.id] && !attendees[item.id]?.length" title="No registrations yet" message="Attendees will appear here after registering." /></details></div></article>
          </template>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { nextTick, onMounted, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import apiClient from '../services/api'
import RoboticsLoader from '../components/RoboticsLoader.vue'
import StatusBadge from '../components/StatusBadge.vue'
import EmptyState from '../components/EmptyState.vue'

const userStore = useUserStore()
const router = useRouter()

onMounted(async () => {
  if (!userStore.isAuthenticated) {
    await userStore.fetchCurrentUser()
  }
  if (!userStore.isAuthenticated) {
    router.replace('/login')
    return
  }
  await loadContent()
})

const user = userStore.user
const members = ref([])
const events = ref([])
const images = ref([])
const message = ref('')
const isError = ref(false)
const contentLoading = ref(true)
const uploadStatus = reactive({ member: '', gallery: '', event: '' })
const uploadProgress = reactive({ member: 0, gallery: 0, event: 0 })
const attendees = reactive({})
const attendeesLoaded = reactive({})
const attendeeLoading = reactive({})
const memberEditor = ref(null)
const eventEditor = ref(null)
const memberPanel = ref(null)
const eventPanel = ref(null)
const memberForm = reactive({ name: '', role: '', description: '', skills: '', image_url: '' })
const eventForm = reactive({ title: '', date: '', category: '', location: '', description: '', image_url: '', registration_url: '', max_attendees: null })
const imageForm = reactive({ image_url: '', caption: '', category: 'general' })
const fresh = (form, defaults) => Object.assign(form, defaults)
function reportError(error) {
  isError.value = true
  const details = error.response?.data?.details
  message.value = details ? Object.values(details).join(' ') : (error.response?.data?.error || error.message || 'Could not save changes.')
}
const isUploading = (kind) => uploadStatus[kind].startsWith('Uploading')
async function editMember(item) {
  Object.assign(memberForm, { ...item, skills: Array.isArray(item.skills) ? item.skills.join(', ') : item.skills || '' })
  if (memberPanel.value) memberPanel.value.open = true
  await nextTick(); memberEditor.value?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}
async function editEvent(item) {
  const localDate = new Date(item.date)
  const offsetDate = new Date(localDate.getTime() - localDate.getTimezoneOffset() * 60000).toISOString().slice(0, 16)
  Object.assign(eventForm, { ...item, date: offsetDate })
  if (eventPanel.value) eventPanel.value.open = true
  await nextTick(); eventEditor.value?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}
async function uploadImage(event, form) {
  const file = event.target.files?.[0]
  if (!file) return
  const data = new FormData(); data.append('file', file)
  const kind = form === memberForm ? 'member' : (form === imageForm ? 'gallery' : 'event')
  isError.value = false; uploadStatus[kind] = 'Uploading image (0%)'; uploadProgress[kind] = 0
  try {
    const response = await apiClient.post('/uploads', data, { headers: { 'Content-Type': 'multipart/form-data' }, onUploadProgress: (progress) => { uploadProgress[kind] = progress.total ? Math.round(progress.loaded * 100 / progress.total) : 0; uploadStatus[kind] = `Uploading image (${uploadProgress[kind]}%)` } })
    form.image_url = response.data.image_url
    uploadStatus[kind] = 'Upload complete'; uploadProgress[kind] = 100
  } catch (error) { uploadStatus[kind] = ''; reportError(error) }
}
async function loadContent() {
  if (!userStore.isAdmin) { contentLoading.value = false; return }
  contentLoading.value = true
  try {
    const [team, eventList, gallery] = await Promise.all([apiClient.get('/team'), apiClient.get('/events'), apiClient.get('/gallery')])
    members.value = team.data; events.value = eventList.data; images.value = gallery.data
  } catch (error) { reportError(error) } finally { contentLoading.value = false }
}
async function loadAttendees(eventId) {
  attendeeLoading[eventId] = true
  try { const { data } = await apiClient.get(`/events/${eventId}/attendees`); attendees[eventId] = data; attendeesLoaded[eventId] = true } catch (error) { reportError(error) } finally { attendeeLoading[eventId] = false }
}
async function reorder(list, index, direction, endpoint) {
  const other = index + direction
  if (other < 0 || other >= list.length) return
  ;[list[index], list[other]] = [list[other], list[index]]
  try {
    await Promise.all(list.map((item, order) => { item.sort_order = order; return apiClient.put(`${endpoint}/${item.id}`, { sort_order: order }) }))
    isError.value = false; message.value = 'Display order updated.'
  } catch (error) { reportError(error); await loadContent() }
}
async function saveMember() {
  try {
    const data = { ...memberForm, skills: memberForm.skills.split(',').map((skill) => skill.trim()).filter(Boolean) }
    if (data.id) await apiClient.put(`/team/${data.id}`, data); else await apiClient.post('/team', data)
    fresh(memberForm, { id: null, name: '', role: '', description: '', skills: '', image_url: '' }); isError.value = false; message.value = 'Team member saved.'; await loadContent()
  } catch (error) { reportError(error) }
}
async function saveImage() {
  try { await apiClient.post('/gallery', imageForm); fresh(imageForm, { image_url: '', caption: '', category: 'general' }); isError.value = false; message.value = 'Image added.'; await loadContent() } catch (error) { reportError(error) }
}
async function saveEvent() {
  try {
    const data = { ...eventForm, date: new Date(eventForm.date).toISOString(), max_attendees: eventForm.max_attendees === '' ? null : (eventForm.max_attendees ?? null) }
    if (data.id) await apiClient.put(`/events/${data.id}`, data); else await apiClient.post('/events', data)
    fresh(eventForm, { id: null, title: '', date: '', category: '', location: '', description: '', image_url: '', registration_url: '', max_attendees: null }); isError.value = false; message.value = 'Event saved.'; await loadContent()
  } catch (error) { reportError(error) }
}
async function remove(endpoint, id, list) {
  if (!window.confirm('Delete this item? This cannot be undone.')) return
  try { await apiClient.delete(`${endpoint}/${id}`); list.splice(list.findIndex((item) => item.id === id), 1); isError.value = false; message.value = 'Item removed.' } catch (error) { reportError(error) }
}
</script>

<style scoped>
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
.dashboard-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 28px;
}
.dashboard-card h3 {
  margin-bottom: 14px;
}
.dashboard-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 10px;
}
.dashboard-card a {
  color: var(--accent-cyan);
}
.editor { display: grid; gap: 10px; align-content: start; }
.editor input, .editor textarea { width: 100%; padding: 10px; color: var(--text); background: var(--bg); border: 1px solid var(--border); border-radius: 8px; }
.editor-message { margin-top: 18px; }
.editor-error { color: #fb7185; }
.managed-row { display:flex; align-items:center; justify-content:space-between; gap:10px; padding:7px 0; border-bottom:1px solid var(--border); }
.row-actions { display:flex; gap:5px; flex-shrink:0; }
.icon-action { width:34px; height:34px; display:inline-grid; place-items:center; border:1px solid var(--border); border-radius:8px; background:transparent; color:var(--amber); cursor:pointer; }
.icon-action:hover { background:rgba(245,158,11,.12); }
.icon-action svg { width:17px; height:17px; fill:none; stroke:currentColor; stroke-width:1.8; stroke-linecap:round; stroke-linejoin:round; }
.delete-action { color:#fb7185; }
.delete-action:hover { background:rgba(251,113,133,.12); }
.image-preview { max-width:140px; max-height:100px; object-fit:cover; border-radius:8px; }
.event-admin-row { padding:8px 0; border-bottom:1px solid var(--border); }
.managed-content > .dashboard-card { height:460px; overflow-y:auto; scrollbar-width:thin; scrollbar-color:var(--accent-cyan) rgba(148,163,184,.12); }
.managed-content > .dashboard-card::-webkit-scrollbar { width:6px; }
.managed-content > .dashboard-card::-webkit-scrollbar-thumb { background:rgba(34,211,238,.42); border-radius:9px; }
.managed-content > .dashboard-card::-webkit-scrollbar-track { background:rgba(148,163,184,.08); }
.dashboard-grid:not(.managed-content):not(.editor-panels) > .dashboard-card { height:190px; overflow-y:auto; scrollbar-width:thin; scrollbar-color:var(--accent-cyan) rgba(148,163,184,.12); }
.attendee-list { padding:8px 0; color:var(--text-dim); }
.attendee-list summary { cursor:pointer; color:var(--accent-cyan); }
.icon-action:disabled { opacity:.35; cursor:not-allowed; }
.editor-panels { margin-bottom:24px; }
.admin-form-panel { min-width:0; }
.admin-form-panel > summary { position:relative; display:grid; gap:4px; padding:16px 18px; border:1px solid var(--border); border-radius:12px; background:linear-gradient(130deg,rgba(34,211,238,.07),rgba(245,158,11,.035)); color:var(--text-primary); font:1.25rem 'Bebas Neue',sans-serif; letter-spacing:.06em; cursor:pointer; list-style:none; }
.admin-form-panel > summary::-webkit-details-marker { display:none; }
.admin-form-panel > summary::after { content:'+'; position:absolute; right:18px; top:10px; color:var(--accent-cyan); font:1.5rem 'DM Mono',monospace; }
.admin-form-panel[open] > summary::after { content:'−'; color:var(--amber); }
.admin-form-panel[open] { height:460px; display:block; overflow-y:auto; scrollbar-width:thin; scrollbar-color:var(--accent-cyan) rgba(148,163,184,.12); }
.admin-form-panel[open]::-webkit-scrollbar { width:6px; }
.admin-form-panel[open]::-webkit-scrollbar-thumb { background:rgba(34,211,238,.42); border-radius:9px; }
.admin-form-panel[open]::-webkit-scrollbar-track { background:rgba(148,163,184,.08); }
.admin-form-panel[open] > summary { position:sticky; top:0; z-index:2; }
.admin-form-panel > summary span { color:var(--text-muted); font: .68rem 'DM Mono',monospace; letter-spacing:.05em; }
.admin-form-panel .editor { min-height:0; overflow:visible; margin-top:10px; }
.editor small { color:var(--text-dim); }
.editor progress { width:100%; height:4px; accent-color:var(--accent-cyan); }
</style>
