<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Broom_.svg">
    <GamesList msg="Welcome to GamesList"/>
  </div>
</template>

<script>
// @ is an alias to /src
import GamesList from '@/components/GamesList.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    GamesList
  },
  methods: {
    getDecks: function () {
      axios.get('localhost:3306').then((response) => {
      console.log(response.data)
      })
    }
  },
  mounted: function () {
    this.getDecks()
  }
}
</script>
