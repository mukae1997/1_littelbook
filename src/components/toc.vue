<template>
  <div class="toc">
   <h3> TOC </h3>
   <div id="info">
    <h4>info</h4>
     <div>{{work.name}}</div>
       <div>{{work.publish_year}}</div>
         <div>{{work.type}}</div>
   </div>


    <sub-toc v-bind:subtoc="work.content" />


  </div>
</template>

<script>
import {bus} from '../main'
// Essays_and_Lectures
import workData from '../.././literature/Essays_and_Lectures.json'
import subToc from './subtoc.vue'
export default {
 components: {
  'sub-toc': subToc
 },
data () {
  return {
   work: workData,
   currentChapterName: '',
   deepLevel: false
  }
},
  created() {
   var getArrayWhereTheNameIn  = function self(name, thing) {
    // console.log(thing);
     console.log( thing);
     for( var key in thing) {
     var names = Object.keys(thing[key]);

    for (var i = 0; i < names.length; i++) {
     var k = names[i];
     // console.log(k == name,'[',k,']', '[',name,']');
     if (k==name) {
      return thing;
     }
     if (!Array.isArray(thing[key][k])) {
      var res = self(name, thing[key][k]);
      if (res != []) return res;
     }
     if (Object.keys(thing[key][k]).indexOf(name) != -1) {
      return thing;
     }
    }
     }
    return [];
   };

   bus.$on('callSibling', (obj)=>{
    console.log('high level receive a call.');
    var name = obj.name;
    var pointer = obj.pointer;
    console.log(name);
    var arr = getArrayWhereTheNameIn(name, this.work.content);
    console.log(arr);

   });
  },
  beforeMounted() {
  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#info div {
 padding:5px;
}
div {
 border:1px dotted #ccc;
}
.toc {
 text-align: left;
}
</style>
