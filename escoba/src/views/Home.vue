<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Broom_.svg">
    <DeckTable />
    <GamesList msg="Welcome to GamesList"/>
  </div>
</template>

<script>
// @ is an alias to /src
import GamesList from '@/components/GamesList.vue'
import DeckTable from '@/components/DeckTable.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    GamesList,
    DeckTable
  },
  methods: {
    // getDecks: function () {
    //   axios.get('localhost:3306').then((response) => {
    //   console.log(response.data)
    //   })
    // }
  },
  mounted: function () {
    // this.getDecks()
  }
}
</script>
