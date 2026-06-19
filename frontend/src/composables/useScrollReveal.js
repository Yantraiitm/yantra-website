import { onMounted, onBeforeUnmount, onUpdated, nextTick } from 'vue'

export function useScrollReveal() {
  let io
  let mutationObserver

  const observeRevealElements = () => {
    if (!io) return

    document.querySelectorAll('.reveal').forEach((el, i) => {
      if (el.dataset.revealBound === 'true') return

      el.dataset.revealBound = 'true'
      el.style.transitionDelay = (i % 5) * 0.07 + 's'
      io.observe(el)
    })
  }

  const forceRevealAll = () => {
    document.querySelectorAll('.reveal').forEach((el) => {
      el.classList.add('visible', 'in')
      el.dataset.revealBound = 'true'
    })
  }

  onMounted(async () => {
    await nextTick()

    if (!('IntersectionObserver' in window)) {
      forceRevealAll()
      return
    }

    io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          entry.target.classList.add('in')
          io.unobserve(entry.target)
        }
      })
    }, { threshold: 0.1, rootMargin: '0px 0px -28px 0px' })

    mutationObserver = new MutationObserver(() => {
      requestAnimationFrame(observeRevealElements)
    })

    mutationObserver.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['class']
    })

    observeRevealElements()
  })

  onUpdated(() => {
    requestAnimationFrame(() => {
      if (!io) return
      document.querySelectorAll('.reveal').forEach((el) => {
        if (!el.dataset.revealBound) {
          el.dataset.revealBound = 'true'
          el.style.transitionDelay = '0s'
          io.observe(el)
        }
      })
      observeRevealElements()
    })
  })

  onBeforeUnmount(() => {
    if (io) io.disconnect()
    if (mutationObserver) mutationObserver.disconnect()
  })
}
