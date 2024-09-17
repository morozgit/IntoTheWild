<template>
  <div class="location-card" @click="goToDetail">
    <img :src="imageSrc" alt="Location Image" />
    <h3>{{ location.name }}</h3>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    location: {
      type: Object,
      required: true
    }
  },
  computed: {
    imageSrc() {

      return this.location.image;
    }
  },
  methods: {
    async fetchAllLocations() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/location/images');
        this.locations = response.data;
        console.log('Locations fetched:', this.locations.image);
      } catch (error) {
        console.error('Error fetching locations:', error);
      }
    },
    goToDetail() {
      this.$router.push({ name: 'LocationDetail', params: { location_id: this.location.image } });
    }
  }
}
</script>

<style scoped>
.location-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px;
  cursor: pointer;
  text-align: center;
}

.location-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
</style>
