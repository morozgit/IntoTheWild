<template>
  <div class="location-list">
    <LocationCard v-for="location in locations" :key="location.id" :location="location" />
  </div>
</template>

<script>
import LocationCard from '@/components/LocationCard.vue';

export default {
  components: {
    LocationCard
  },
  data() {
    return {
      locations: [
        { id: 1, name: 'Горный Алтай', image: 'Gorniy-Altay.png' },
        { id: 2, name: 'Шерегеш', image: 'sheregesh.png' }
      ]
    };
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
