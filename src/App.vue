<template>
  <div id="app">
   <h1> little book</h1>
   <router-view />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Book from './components/Book'
import BookList from './components/booklist.vue'
export default {
  name: 'app',
  components: {
    Book,
    BookList
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
</style>
