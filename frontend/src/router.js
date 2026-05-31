import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from './stores/user'

// Pages
import Home from './pages/Home.vue'
import About from './pages/About.vue'
import Team from './pages/Team.vue'
import Projects from './pages/Projects.vue'
import Courses from './pages/Courses.vue'
import Events from './pages/Events.vue'
import Gallery from './pages/Gallery.vue'
import Blog from './pages/Blog.vue'
import Join from './pages/Join.vue'
import Contact from './pages/Contact.vue'
import Login from './pages/Login.vue'
import Dashboard from './pages/Dashboard.vue'
import NotFound from './pages/NotFound.vue'

const routes = [
  { path: '/', component: Home, meta: { title: 'Home' } },
  { path: '/about', component: About, meta: { title: 'About' } },
  { path: '/team', component: Team, meta: { title: 'Team' } },
  { path: '/projects', component: Projects, meta: { title: 'Projects' } },
  { path: '/courses', component: Courses, meta: { title: 'Courses' } },
  { path: '/events', component: Events, meta: { title: 'Events' } },
  { path: '/gallery', component: Gallery, meta: { title: 'Gallery' } },
  { path: '/blog', component: Blog, meta: { title: 'Blog' } },
  { path: '/join', component: Join, meta: { title: 'Join' } },
  { path: '/contact', component: Contact, meta: { title: 'Contact' } },
  { path: '/login', component: Login, meta: { title: 'Login' } },
  { path: '/dashboard', component: Dashboard, meta: { title: 'Dashboard', auth: true } },
  { path: '/:pathMatch(.*)*', component: NotFound, meta: { title: 'Not Found' } }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

router.beforeEach(async (to, from, next) => {
  document.title = `${to.meta.title} | Yantra Robotics Society`

  const userStore = useUserStore()
  if (to.meta.auth && !userStore.isAuthenticated) {
    try {
      await userStore.fetchCurrentUser()
    } catch {}
  }

  if (to.meta.auth && !userStore.isAuthenticated) {
    return next('/login')
  }

  if (to.path === '/login' && userStore.isAuthenticated) {
    return next('/dashboard')
  }

  next()
})

export default router
