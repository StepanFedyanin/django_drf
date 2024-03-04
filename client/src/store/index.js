import { createStore } from 'vuex'
import VuexPersist from 'vuex-persist';


const vuexPersist = new VuexPersist({
  key: 'restaurant-key',
  //storage: window.localStorage
});

export default createStore({
  state () {
    return {
      token: null,
      user: null,
    }
  },
  plugins: [vuexPersist.plugin],
  mutations: {
    user(state, user) {
      state.user = user;
    },
    setToken(state, tokens) {
      state.token = tokens;
    },
  },
  actions: {
    setToken(context, tokens) {
      context.commit('setToken', tokens);
    },
  }
});
