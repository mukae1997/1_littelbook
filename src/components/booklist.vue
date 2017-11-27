<template>
  <div id="booklist">
   <h1> book list </h1>
   <div id="maincontainer">
    <div id="mainlist" class ='container'>
     <h5>I am mainlist </h5>
     <transition-group tag="ul" name="slide">
      <li v-for = "b in bookList" :key="b.name"
        >
       <div>{{b.name}} </div>
       <div >
        remark:
         <label v-if="b != editedBook || !editing"
         @click="editRemark(b)">{{b.remark}}</label>
       </div>
       <input  type="text"
       v-model="editingRemark"
       v-if="editedBook == b && editing"
       v-on-edit="editedBook == b"
       @keyup.enter="doneEdit(b)"
       @keyup.esc="cancelEdit(b)" />
      </li>
     </transition-group>
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
      remark:"romantic"
     },
      {
       name:'Story Of Your Life',
       remark:"cool"
      }],
      editedRemarkCache:"", // for canceling while preserve content
      editedBook:null,
      editing: false,
      editingRemark:""
    }
  },
  methods: {
   'editRemark': function(b) {
    // console.log(b);
     console.log('editRemark');
    var deepCopyOf = function self(s) {
     return (' '+s).slice(1);
    };
   this.editingRemark = deepCopyOf(b.remark);
    // console.log(this.editingRemark);
    this.editedRemarkCache = b.remark;
    this.editedBook = b;
    this.editing = true;
    console.log(this.bookList[0]);
   },
   'doneEdit': function(b) {
    console.log('blur');
    b.remark = this.editingRemark;
    this.editing = false;
   },
   'cancelEdit': function(b) {
   console.log(this.bookList[0]);
    console.log('cancelEdit');
    // b.remark = this.editedRemarkCache; // useless
    this.editedRemarkCache = "";
    this.editing = false;
   }
  },
  watch: {
   bookList: function(newBookList) {
    console.log(newBookList);
   }
  },
  directives: {
   'on-edit': {
    bind(el,binding,vnode) {
     if (binding.value) {
      el.focus();
     }
    }
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
 padding: 15px;
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
