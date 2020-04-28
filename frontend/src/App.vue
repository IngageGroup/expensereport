<template>
  <div id="app">

      Last Name:
      <input type="text" v-model="lastname" id="lastname"/>


      First Name:
      <input type="text" v-model="firstname" id="firstname"/>
 
    <UploadWidget />
  </div>
</template>

<script>
import UploadWidget from "./components/UploadWidget"
export default {
  name: "App",
  components: {
    UploadWidget
  }
};
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
