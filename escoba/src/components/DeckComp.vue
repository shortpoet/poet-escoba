<template>
  <div class="deck-comp">
    <div v-if="getDeckLoaded">
      <b-button
        @click="post()"
      >
        Post
      </b-button>
      <hr />
      <CardComp
        v-for="(card, i) in getDeck"
        :key="i"
        :card="card"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import CardComp from '@/components/CardComp'
import axios from 'axios'

var config = { headers: {  
                      'Content-Type': 'application/json',
                      'Access-Control-Allow-Origin': '*'}
             }

export default {
  name: 'DeckComp',
  components: {
    CardComp  
  },
  props: {
    msg: String
  },
  computed: {
    ...mapGetters([
      'getDeckLoaded',
      'getDeck',
      'getCards',
      'getDeckOrder'
    ])
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
    },
    post: function () {
      axios
        .post("http://127.0.0.1:5000/makedeck", 
          { label : "Test" , text : "Test"} , config)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  },
  mounted: function() {
    this.log(this.getDeckOrder)
    if(this.getDeckLoaded) {
      console.log(this.getCards)
      console.log(this.getDeck)
    }
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
