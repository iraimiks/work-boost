import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      data: [],
    },
    page: 0
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
      state.page = 1;
    },
    addToData(state, item) {
      state.user.data.push(item)
      localStorage.setItem('user', JSON.stringify(state.user))
    },
    pageNum(state, item) {
      console.log("state", item)
      state.page = item;
    }
  },
  actions: {
  },
  modules: {
  }
})
