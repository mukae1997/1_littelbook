<template>
  <div class="toc">
   <h3> TOC </h3>
   <div id="info">
    <h4>info</h4>
     <div>{{work.name}}</div>
       <div>{{work.publish_year}}</div>
         <div>{{work.type}}</div>
   </div>
    <ul>
     <li>
       <div class='toc' v-on:click="clickChapter" v-for="(c,index) in work.content">
        {{index}}
        <ul v-if="!Array.isArray(Object.values(work.content)[0])">
         <li  v-for = "(deepc,deepi) in work.content[index]">
          {{deepi}}
         </li>
        </ul>
       </div>
      </li>
    </ul>


  </div>
</template>

<script>
import {bus} from '../main'
import workData from '../.././literature/Essays_and_Lectures.json'
export default {

  created() {
   bus.$on('pageChanged', (id)=> {

   console.log('pageChanged: ', '[',id,']');
   var pointer = (id == 'prev')?-1:1;
   var cts = this.work['content'];
   while (cts[this.currentChapterName] == null){
   // console.log('\n\n',this.currentChapterName);
   //  console.log(this.work['content'][this.currentChapterName]);
    cts = Object.values(this.work['content'])[0];
    console.log( cts);
   }

    var targetIndex = Object.keys(cts).indexOf(this.currentChapterName) + pointer;
    // console.log(Object.keys(cts).length, 'Object.keys(cts).length');
    if (targetIndex >= 0 && targetIndex < Object.keys(cts).length) {
     var chp = Object.keys(cts)[targetIndex];
      this.currentChapterName = chp;
     bus.$emit('chapterChanged', {
      chapterName: chp,
      content: cts[chp]
     });
    }


  });
  },
  mounted(){
    this.deepLevel = !Array.isArray(Object.values(this.work['content'])[0]);
     // console.log(this.deepLevel);
  },
  beforeMounted() {
  },
  data () {
    return {
     work: workData,
     currentChapterName: '',
     deepLevel: false
    }
  },
  methods: {
   'clickChapter':function(e) {
    // find the chapter
    console.log(e.target.textContent.match(/[\w\d\.-_]+\s*[\w\d\.-_]+[^\n]/g));
     var chp = e.target.textContent.match(/[\w\d\.-_]+\s*[\w\d\.-_]+[^\n]/g).join().replace(',' ,'');
     this.currentChapterName = chp;
     console.log(chp, typeof(this.work['content'][chp]));
     var mes = {};
      var cts = this.work['content'][chp];
     if (Array.isArray(cts)) {
     mes = {
      content:cts,
      chapterName: chp
     };
    } else if (cts){
     mes = {
      content: Object.keys(cts),
      chapterName: chp
     }
    } else {
     // undefined
     if (cts == null){
      cts = Object.values(this.work['content'])[chp];
       console.log(  Object.values(this.work['content']));
     }
      mes = {
       content: cts,
       chapterName: chp
      }
    }

     bus.$emit('chapterChanged', mes);
   }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
 border:1px dotted #ccc;
}
.toc {
 text-align: left;
}
</style>
