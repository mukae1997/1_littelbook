<template>
  <div id="app">
   <h1> little book</h1>
   <nav>
    <router-link to="/" exact> Home .</router-link>
       <ul id="books-in-reading">
        <li>
        <router-link to="/read"  exact> Essays_and_Lectures .</router-link>
       </li>
        <li>
        <router-link to="/read2" exact> Happy Prince .</router-link>
       </li>
       </ul>
   </nav>
   <router-view />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Book from './components/Book'
import BookList from './components/booklist.vue'
import EAL from '.././literature/Essays_and_Lectures.json'
export default {
  name: 'app',
  components: {
    Book,
    BookList
  },
  data(){
   return {
    eal:EAL
   }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
nav li {
 display: inline-block;
 padding: 10px;
 background-color: #bbb;
 border-radius: 10px;
}
router-link {
 font-size: 18px;
}
</style>
