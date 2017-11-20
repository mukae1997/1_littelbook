<template>
  <div class="subtoc">

    <ul>
     <li v-on:click="clickChapter" v-for="(c,index) in toc">
       <div  >
        {{index}}
         <sub-toc  v-if="!Array.isArray(c)"
           v-bind:subtoc="c"  v-bind:chapName="index" > </sub-toc>
       </div>
      </li>
    </ul>


  </div>
</template>

<script>
import {bus} from '../main'
export default {
 name: 'sub-toc',
 props:{
  subtoc: {
   type:Object
  },
  chapName: {
   type:String
  }
 },
  created() {
   this.toc = this.subtoc;
   this.chapterName = this.chapName;
   // console.log(Array.isArray(Object.values(this.toc)[0]));
   bus.$on('shoutForSibling', (name)=>{
    if (name == this.chapterName) {
     // answer the call
    }
   });
   if (Array.isArray(Object.values(this.toc)[0])) {
    this.tocReadable = true;
    // console.log(this.toc);
    bus.$on('pageChanged', (id)=> {

    console.log('pageChanged: ', '[',id,']');
    var pointer = (id == 'prev')?-1:1;
    var cts = this.toc;

    var findID = Object.keys(cts).indexOf(this.chapterName);
     if (findID != -1) {
          var targetIndex =  findID + pointer;
          if (!((findID == 0 && pointer == -1)
          || (findID == Object.keys(cts).length-1 && pointer == 1))) {

           var chp = Object.keys(cts)[targetIndex];
            this.chapterName = chp;
           bus.$emit('chapterChanged', {
            chapterName: chp,
            content: cts[chp]
           });
          } else {
           // need to change chapter
           // console.log('findID = ',findID);
           bus.$emit('callSibling', {
            name: this.chapterName,
            pointer: pointer
           });
          }
     }


   });
   }
  },
  data () {
    return {
     toc:{},
     chapterName: '',
     tocReadable:false
    }
  },
  methods: {
   'clickChapter':function(e) {
    if　(this.tocReadable) {

      var chp =　e.target.textContent.match(/[^\n\s].*[^\n\s]/g)[0];
      this.chapterName = chp;

      var mes = {};
       var cts = this.toc[chp];
      if (cts){
      mes = {
       content: cts,
       chapterName: chp
      };


      bus.$emit('chapterChanged', mes);
    }

   }
  }
 }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
font-size:8;
 border:1px dotted #ccc;
}
.toc {
 text-align: left;
}
</style>
