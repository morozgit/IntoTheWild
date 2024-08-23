<!-- src/components/LocationCard.vue -->
<template>
    <div class="card">
      <img :src="imgSrc" :alt="title" class="image"/>
      <h2 class="card-title">{{ title }}</h2>
      <p class="card-description">{{ description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      imgSrc: String,
      title: String,
      description: String,
    },
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #fff;
    padding: 16px;
    border-radius: 18px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }
  .image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 12px;
    margin-bottom: 16px;
  }
  .card-title {
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 8px;
  }
  .card-description {
    color: #333;
  }
  </style>
  