<template>
  <div id="booklist">
   <h1> book list </h1>
   <div id="maincontainer">
    <div id="mainlist" class ='container'>
     <h5>I am mainlist </h5>
     <ul>
      <li v-for = "b in bookList">
       <div>{{b.name}} </div>
       <div>
         <label @dbclick="editRemark(b)">{{b.remark}}</label>
       </div>
      </li>
     </ul>
    </div>

   <div id="searchbox-container" class ='container'>
    <input id="searchbox" type = "text"
     placeholder="Search for book..."></input>
   </div>
  </div>
     </div>
</template>

<script>

export default {
  data () {
    return {
     bookList: [{
      name:'Tender is the night',
      remark:""
     },
      {
       name:'Story Of Your Life',
       remark:""
      }]
    }
  },
  methods: {
   'editRemark': function() {

   }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
 border:1px dotted #ccc;
}
#searchbox-container{
 padding:20px;
}
li div {
 padding-left: 10px;
 display: inline-block;
}
.container {
 display: inline-block;
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
