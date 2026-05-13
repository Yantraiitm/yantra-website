import { onMounted, nextTick } from 'vue'

export function useScrollReveal() {
  onMounted(async () => {
    await nextTick()
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible')
          e.target.classList.add('in')
          io.unobserve(e.target)
        }
      })
    }, { threshold: 0.1, rootMargin: '0px 0px -28px 0px' })

    document.querySelectorAll('.reveal').forEach((el, i) => {
      el.style.transitionDelay = (i % 5) * 0.07 + 's'
      io.observe(el)
    })
  })
}
