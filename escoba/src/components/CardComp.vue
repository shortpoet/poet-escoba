<template>
  <div class="card-comp">
    <div v-if="getDeckLoaded">
      <b-container>
        <b-row>
          <b-col md="2"></b-col>
          <b-col md="8">
            <b-card 
              style="max-width: 20rem; height: 25rem"
            >
              <v-icon
                v-for="(value, i) in card.value"
                :key="i" 
                :name="iconName"
              ></v-icon>
            </b-card>
          </b-col>
          <b-col md="2"></b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'CardComp',
  props: {
    card: Object
  },
  computed: {
    ...mapGetters([
      'getDeckLoaded',
      'getDeck'
    ]),
    iconName: function () {
      if (this.card.suit === 'O') {
        return 'brands/bitcoin'
      }
      if (this.card.suit === 'B') {
        return 'hammer'
      }
      if (this.card.suit === 'C') {
        return 'trophy'
      }
      if (this.card.suit === 'E') {
        return 'screwdriver'
      }
    }
  },
  methods: {
    log: function(input) {
      var comp = this
      if(input) {
        console.log(input)
      }
      else {
        console.log(comp)
      }
    }
  },
  mounted: function() {
    // this.log(this.getDeck)
    // if(this.getDeckLoaded) {
    //   console.log(this.getDeck)
    // }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
