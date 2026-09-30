import { ref } from 'vue'

export const activeApiRequests = ref(0)

export function beginApiRequest(config) {
  if (!config.__networkTracked) {
    config.__networkTracked = true
    activeApiRequests.value += 1
  }
}

export function endApiRequest(config) {
  if (config?.__networkTracked) {
    config.__networkTracked = false
    activeApiRequests.value = Math.max(0, activeApiRequests.value - 1)
  }
}
