<template>
    <div class="bottom-bar">
      <button @click="goContact">
        <img src="@/assets/envelope.svg" alt="Contact" class="icon" />
      </button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goContact() {
        this.$router.push({ name: 'Contact' });
      }
    }
  }
  </script>
  
  <style scoped>
  .bottom-bar {
    background-color: #42b983; /* Зеленый фон */
    padding: 10px;
    display: flex;
    justify-content: center; /* Выравнивание кнопок по центру контейнера */
    align-items: center;
    gap: 20px;
    position: fixed; /* Закрепление внизу страницы */
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 1000; /* Чтобы панель была выше остальных элементов */
  }
  
  
  .bottom-bar button {
    background: none; /* Без фона */
    border: none;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
  }
  
  .bottom-bar button .icon {
    width: 24px;
    height: 24px;
    fill: white; /* Цвет иконки */
  }
  </style>
  