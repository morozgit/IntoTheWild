<template>
  <div class="top-bar">
    <button @click="goHome" class="logo-button">
      <span class="logo-text">Into the Wild</span>
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    goHome() {
      this.$router.push({ name: 'Home' });
    }
  }
}
</script>

<style scoped>
.top-bar {
  background-color: #42b983; /* Зеленый фон */
  padding: 10px;
  display: flex;
  justify-content: center; /* Выравнивание кнопок по центру контейнера */
  align-items: center;
  gap: 20px;
  position: fixed; /* Закрепление панели */
  top: 0; /* Расположение панели вверху */
  left: 0; /* Расположение панели слева */
  width: 100%; /* Ширина панели на всю ширину экрана */
  z-index: 1000; /* Убедитесь, что панель находится поверх другого контента */
}

.logo-button {
  display: flex;
  align-items: center;
  justify-content: center; /* Центрирование содержимого кнопки */
  background: none;
  border: none;
  padding: 0;
}

.logo-text {
  font-family: 'Matemasie-Regular'; 
  font-size: 30px;
  font-weight: bold;
  color: black;
}
</style>
