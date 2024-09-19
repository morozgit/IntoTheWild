<template>
  <div class="location-list">
    <LocationCard v-for="location in locations" :key="location.id" :location="location" />
  </div>
</template>

<script>
import LocationCard from '@/components/LocationCard.vue';
import axios from "axios";

export default {
  components: {
    LocationCard
  },
  data() {
    return {
      locations: []
    };
  },
  methods: {
    async fetchAllLocations() {
      try {
        const response = await axios.get('http://31.129.44.137/api/location/all_location');
        this.locations = response.data;
        console.log('Locations fetched:', this.locations);
      } catch (error) {
        console.error('Error fetching locations:', error);
      }
    }
  },
  mounted() {
    this.fetchAllLocations();
  }
}
</script>

<style scoped>
.location-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding-top: 60px; /* Отступ сверху */
  padding-bottom: 60px; /* Отступ снизу */
}
</style>
