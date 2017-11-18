<template>
  <div id="app">
  <Book />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Book from './components/Book'
export default {
  name: 'app',
  components: {
    Book
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
