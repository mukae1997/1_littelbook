<template>
  <div id="book">
   <h2> book </h2>
   <div id='mainpage'>
       <div id = "reader" class="inlinecontainer">
       <reader />
       </div>
          <div id = "toc" class="inlinecontainer">
           <toc />
          </div>
    </div>
  </div>
</template>

<script>
import workData from '../.././literature/1.json'
import toc from './toc.vue'
import reader from './reading.vue'
export default {
 components: {
   'toc':toc,
   'reader':reader,
   chapterChoose: ''
 },
 created() {
  // request to server
 },
 mounted() {
  // console.log(workData);
 },
  data () {
    return {
     work: workData
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
 border:1px dotted #ccc;
}
#mainpage {
 width:800px;
 background-color: #ddd;
 margin:auto;
 padding:50px;
}
.inlinecontainer {
 display: inline-block;
 background-color: #eee;
}
#toc {
 width:25%;
    vertical-align: top;
}
#reader {
 width:60%;
 height:auto;
}
</style>
