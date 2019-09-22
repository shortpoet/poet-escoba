import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    deckLoaded: false,
    deckErrored: false,
    deckData: []
  },
  getters: {
    getCards: function(state) {
      var cards = []
      // console.log(Object.entries(state.deckData.cards))
      Object.entries(state.deckData.cards).forEach((v, i, a) => {
        cards.push(v[0])
      })
      return cards
    },
    getDeck: function(state) {
      var deck = []
      // console.log(Object.entries(state.deckData.cards))
      Object.entries(state.deckData.cards).forEach((v, i, a) => {
        var [a,b,c] = v[1]
        deck.push({'suit': a, 'value': b, 'owner': c})
      })
      return deck
    },
    getDeckLoaded: (state) => {
      return state.deckLoaded
    }
  },
  mutations: {
    changeDeckErrored: function(state, errored) {
      state.deckErrored = errored
    },
    changeDeckLoaded: function(state, loaded) {
      state.deckLoaded = loaded
    },
    initData: function (state, data) {
      state.deckData = data
    },
  },
  actions: {
    loadDeck: function ({ commit, state }) {
      axios.get('http://127.0.0.1:5000/makedeck')
        .then(function(response) {
          console.log(response)
          commit('initData', response.data)
        })
        .catch(function(error) {
          console.log(error)
          commit('changeDeckErrored', true)
        })
        .finally(function() {
          console.log('#### deck finally ####')
          commit('changeDeckLoaded', true)
        })
    }
  }
})
