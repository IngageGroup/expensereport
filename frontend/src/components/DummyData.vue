  
<template>
    <p>Dummy Data from API: {{dataReturned}}</p>
</template>


<script>
import axios from "axios";
export default {
  data() {
    return {
      dataReturned: [],
      errors: []
    };
  },
  async created() {
    let url = `http://localhost:5000/ping`;
    try {
      const response = await axios.get(url);
      this.dataReturned = response.data;
    } catch (e) {
      this.errors.push(e);
    }
  }
  
};
</script>