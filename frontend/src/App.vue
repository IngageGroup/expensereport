<template>
  <div id="app">
    <DummyData>
  </div>
</template>

<script>
import DummyData from './components/DummyData.vue'

export default {
  name: 'App',
  components: {
    DummyData
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
