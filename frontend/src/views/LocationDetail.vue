<template>
  <div class="tracks-section" v-if="tracks.length">
    <h3>Tracks for this location:</h3>
    <!-- Обертка для карточек треков -->
    <div class="track-list">
      <div v-for="track in tracks" :key="track.id" class="track-card">
        <h4>{{ track.name }}</h4>
        <img :src="`/images/${track.image}`" alt="Track Image" />
        <p>{{ track.description }}</p>
      </div>
    </div>
  </div>
  <div v-else>
    <p>No tracks found for this location.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tracks: []
    };
  },
  async mounted() {
    const location_id = this.$route.params.location_id;
    await this.fetchLocationTracks(location_id);
  },
  methods: {
    async fetchLocationTracks(location_id) {
      try {
        const response = await axios.get(`http://localhost:8000/location/${location_id}`);
        this.tracks = response.data;
        console.log('Tracks fetched:', this.tracks);
      } catch (error) {
        console.error('Error fetching tracks:', error);
      }
    }
  }
}
</script>

<style scoped>
.tracks-section {
  padding-top: 20px; /* Отступ сверху */
  padding-bottom: 20px; /* Отступ снизу */
}

.track-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around; /* Равномерное распределение элементов */
  gap: 10px; /* Расстояние между карточками */
}

.track-card {
  border: 1px solid #ddd;
  padding: 10px;
  width: 300px; /* Фиксированная ширина карточек */
  text-align: center;
}

.track-card img {
  width: 100%; /* Изображение занимает всю ширину карточки */
  height: 200px; /* Высота изображения */
  object-fit: cover; /* Обеспечивает, что изображение не искажается */
  border-radius: 8px; /* Добавляет скругление углов для лучшего вида */
}
</style>
