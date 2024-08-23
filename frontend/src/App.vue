<!-- src/components/Webcrumbs.vue -->
<template>
    <div id="webcrumbs"> 
      <div class="container">
        <header class="header">
          <h1 class="title">
            Локации для путешествий
          </h1>
        </header>
      
        <div class="grid-container">
          <LocationCard
            imgSrc="https://tools-api.webcrumbs.org/image-placeholder/250/150/travel/1"
            title="Лучший пляж"
            description="Проведите незабываемый день на этом прекрасном пляже."
          />
          <LocationCard
            imgSrc="https://tools-api.webcrumbs.org/image-placeholder/250/150/travel/2"
            title="Горное озеро"
            description="Поплавайте в чистых водах горного озера, окруженного природой."
          />
          <LocationCard
            imgSrc="https://tools-api.webcrumbs.org/image-placeholder/250/150/travel/3"
            title="Исторический город"
            description="Посетите исторический город с множеством достопримечательностей."
          />
          <LocationCard
            imgSrc="https://tools-api.webcrumbs.org/image-placeholder/250/150/travel/4"
            title="Тропический лес"
            description="Исследуйте густые тропические леса и наслаждайтесь природой."
          />
          <LocationCard
            imgSrc="https://tools-api.webcrumbs.org/image-placeholder/250/150/travel/5"
            title="Северное Сияние"
            description="Наблюдайте за удивительными световыми эффектами северного сияния."
          />
          <LocationCard
            imgSrc="https://tools-api.webcrumbs.org/image-placeholder/250/150/travel/6"
            title="Загородний Домик"
            description="Наслаждайтесь спокойствием и уютом загородного домика."
          />
        </div>
      </div> 
    </div>
  </template>
  
  <script>
  import LocationCard from './LocationCard.vue';
  
  export default {
    components: {
      LocationCard,
    },
  };
  </script>
  
  <style src="./Webcrumbs.css" scoped></style>
  