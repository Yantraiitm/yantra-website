<template>
  <nav id="navbar" :class="{ scrolled: isScrolled }">
    <div class="nav-wrap">
      <RouterLink to="/" class="nav-logo">
        <img src="/img/yantra.png" alt="Yantra Logo" class="logo-mark-img">
        <div>
          <div class="logo-text">YANTRA</div>
          <div class="logo-sub">Robotics Society</div>
        </div>
      </RouterLink>

      <ul class="nav-links" :class="{ open: mobileMenuOpen }">
        <li><RouterLink to="/" @click="closeMobileMenu">Home</RouterLink></li>
        <li><RouterLink to="/about" @click="closeMobileMenu">About</RouterLink></li>
        <li><RouterLink to="/team" @click="closeMobileMenu">Team</RouterLink></li>
        <li><RouterLink to="/projects" @click="closeMobileMenu">Projects</RouterLink></li>
        <li><RouterLink to="/courses" @click="closeMobileMenu">Courses</RouterLink></li>
        <li><RouterLink to="/events" @click="closeMobileMenu">Events</RouterLink></li>
        <li><RouterLink to="/gallery" @click="closeMobileMenu">Gallery</RouterLink></li>
        <li><RouterLink to="/blog" @click="closeMobileMenu">Blog</RouterLink></li>
        <li><RouterLink to="/join" class="nav-join" @click="closeMobileMenu">Join →</RouterLink></li>
        <li><RouterLink to="/contact" @click="closeMobileMenu">Contact</RouterLink></li>
      </ul>

      <button class="hamburger" :class="{ active: mobileMenuOpen }" @click="toggleMobileMenu" aria-label="Toggle navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>
  <!-- backdrop -->
  <div v-if="mobileMenuOpen" class="nav-backdrop" @click="closeMobileMenu"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterLink } from 'vue-router'

const isScrolled = ref(false)
const mobileMenuOpen = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 48
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
#navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 200;
  padding: 18px 0;
  transition: background var(--transition), padding var(--transition), border-color var(--transition);
  border-bottom: 1px solid transparent;
}

#navbar.scrolled {
  background: rgba(14, 14, 14, 0.96);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  padding: 12px 0;
  border-color: var(--border);
}

.nav-wrap {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-mark-img {
  width: 50px;
  height: 50px;
  object-fit: contain;
}

.nav-logo:hover .logo-mark-img {
  filter: brightness(1) invert(0);
  transform: scale(1.05);
}

.logo-text {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.5rem;
  letter-spacing: 0.1em;
  color: var(--text-primary);
  line-height: 1;
}

.logo-sub {
  font-family: 'DM Mono', monospace;
  font-size: 0.52rem;
  color: var(--slate);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2px;
}

.nav-links a {
  font-family: 'DM Mono', monospace;
  font-size: 0.66rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--slate);
  padding: 7px 12px;
  border-radius: 5px;
  transition: color var(--transition), background var(--transition);
}

.nav-links a:hover,
.nav-links a.router-link-active {
  color: var(--amber);
  background: rgba(245, 158, 11, 0.07);
}

.nav-join {
  background: var(--amber) !important;
  color: #0E0E0E !important;
  font-weight: 600 !important;
}

.nav-join:hover {
  background: #D97706 !important;
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 4px;
  background: none;
  border: none;
}

.hamburger span {
  width: 22px;
  height: 2px;
  background: var(--amber);
  border-radius: 2px;
  transition: transform var(--transition), opacity var(--transition);
  display: block;
}

.hamburger.active span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.hamburger.active span:nth-child(2) { opacity: 0; transform: scaleX(0); }
.hamburger.active span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

.nav-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 99;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(2px);
}

@media (max-width: 860px) {
  .nav-backdrop { display: block; }
}

@media (max-width: 860px) {
  .hamburger {
    display: flex;
  }

  .nav-links {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    z-index: 200;
    background: rgba(14, 14, 14, 0.98);
    flex-direction: column;
    padding: 16px;
    gap: 4px;
    border-top: 1px solid var(--border);
    backdrop-filter: blur(14px);
  }

  .nav-links.open {
    display: flex;
  }

  .nav-links a {
    width: 100%;
    text-align: center;
    padding: 11px;
  }
}

@media (max-width: 768px) {
  .logo-mark-img {
    width: 35px;
    height: 35px;
  }
}
</style>
