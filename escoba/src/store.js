import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    deck: []
  },
  mutations: {
    initDeck: function (state, deck) {
      state.deck = deck
    }
  },
  actions: {
    loadDeck: function ({ context, state }) {
      axios.get('http://127.0.0.1:5000/makedeck')
        .then(function(response) {
          console.log(response)
        })
    }
  }
})
