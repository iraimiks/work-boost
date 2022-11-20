import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      data: [],
    },
    hourRate: 0,
    workRate: 0,
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
    },
    addHourRate(state, item) {
      state.hourRate = item;
      localStorage.setItem('hourRate', state.hourRate)
    },
    addWorkRate(state, item) {
      state.workRate = item;
      localStorage.setItem('workRate', state.hourRate)
    }
  },
  actions: {
  },
  modules: {
  }
})
