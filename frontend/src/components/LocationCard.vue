<template>
  <div class="location-card" @click="goToDetail">
    <img :src="imageSrc" alt="Location Image" />
    <h3>{{ location.name }}</h3>
  </div>
</template>

<script>
export default {
  props: {
    location: {
      type: Object,
      required: true
    }
  },
  computed: {
    imageSrc() {
      return `/images/${this.location.image}`;
    }
  },
  methods: {
    goToDetail() {
      this.$router.push({ name: 'LocationDetail', params: { location_id: this.location.id } });
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