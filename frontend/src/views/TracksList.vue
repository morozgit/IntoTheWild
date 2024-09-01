<template>
    <div>
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else-if="track">
        <h1>{{ track.name }}</h1>
        <p>{{ track.description }}</p>
        <img v-if="track.image" :src="imageSrc" alt="Track Image" />
        <p v-else>No image available</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, computed } from 'vue';
  import { useRoute } from 'vue-router';
  import axios from 'axios';
  
  export default {
    name: 'TracksList',
    setup() {
      const route = useRoute();
      const track = ref(null);
      const loading = ref(true);
      const error = ref('');
  
      const locationId = computed(() => route.params.locationId);
  
      const fetchTrack = async () => {
        try {
          console.log(`Fetching data for track ID: ${locationId.value}`);
          const response = await axios.get(`http://localhost:8000/location/${locationId.value}`);
          console.log('API Response:', response.data);
          track.value = response.data; // Проверьте структуру данных
        } catch (err) {
          console.error('Error fetching track:', err.response ? err.response.data : err.message);
          error.value = 'Не удалось загрузить данные';
        } finally {
          loading.value = false;
        }
      };
  
      onMounted(fetchTrack);
  
      const imageSrc = computed(() => {
        // Убедитесь, что путь к изображению корректен
        return track.value ? `/images/${track.value.image}` : '';
      });
  
      return {
        track,
        loading,
        error,
        imageSrc
      };
    }
  };
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
  