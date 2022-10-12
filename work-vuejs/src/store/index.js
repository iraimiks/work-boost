import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      data: []
    }
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('user')) {
        state.user = JSON.parse(localStorage.getItem('user'))
      } else {
        localStorage.setItem('user', JSON.stringify(state.user))
      }
    },
    addToData(state, item) {
      state.user.data.push(item)
      localStorage.setItem('user', JSON.stringify(state.user))
    }
  },
  actions: {
  },
  modules: {
  }
})
