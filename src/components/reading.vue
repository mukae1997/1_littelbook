<template>
  <div class="reader">
   <h3> reader </h3>
   <h4> {{chapterHeader}}</h4>
   <div id="para-container">
    <div class='flip-page' id="prev" v-on:click="pageChange">
     <
    </div>
   <div id='paras'>
    <div class="paragraph" v-for="para in currentChapter"
    v-if="para != null && para.replace(' ','').length != 0" >
      {{para}}  </div>
   </div>
    <div class='flip-page' id="next" v-on:click="pageChange">
     >
    </div>
  </div>
  </div>
</template>

<script>
import {bus} from '../main'
export default {
 created() {
  bus.$on('chapterChanged', (data)=> {
   this.currentChapter = data.content;
   this.chapterHeader = data.chapterName;
  // console.log('response: ', data);
 })
 },
 props:{
 },
  data () {
    return {
     currentChapter:'',
     chapterHeader:''
    }
  },
  methods: {
   'pageChange': function(e) {
    var id = e.target.id;
    bus.$emit('pageChanged', id.replace(' ',''));
   }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.reader {
 vertical-align: top;
}
.paragraph {
 background: #ddd;
 padding:20px;
 text-align: left;
}
#paras {
 padding:10px;
 width:80%
}
#para-container div {
 display:inline-block;
}
.flip-page {
 vertical-align: top;
 font-size: 30px;
 font-weight: bold;
 color:#bbb;
}
</style>
