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
// import {readBooks} from '../read_dir'
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
     for (var key in thing) {
      if (Array.isArray(Object.values(thing[key])[0])) {
       if (Object.keys(thing[key]).indexOf(name) != -1) {
        return {
         arr: Object.keys(thing),
         parent: key
         };
       }
      } else {
       return self(name, thing[k]);
      }
     }
     return [];
   };

   bus.$on('callSibling', (obj)=>{
    console.log('toc level receive a call.');
    var name = obj.name;
    this.currentChapterName = obj.name;
    var pointer = obj.pointer;
    // console.log(name);
    var res = getArrayWhereTheNameIn(name, this.work.content);
    var arr = res.arr;
    // console.log(arr);
    var parentPointer = (res.arr.indexOf(res.parent));
    if (!((parentPointer == 0 && pointer == -1)
    || (parentPointer == res.arr.length-1 && pointer == 1))) {
     var sibliPointer = parentPointer + pointer;
     var sibliName = arr[sibliPointer];
      console.log('toc shout for:', sibliName);
     bus.$emit('shoutForSibling',  {
      name:sibliName,
      pointer: obj.pointer
     });
    }

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
h3 {
 text-align: center;
}
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
