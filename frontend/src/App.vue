<template>
  <div id="app">
    <TopBar />
    <div class="main-content">
      <router-view />
    </div>
    <BottomBar />
  </div>
</template>

<script>
import TopBar from './components/TopBar.vue'
import BottomBar from './components/BottomBar.vue'

export default {
  name: 'App',
  components: {
    TopBar,
    BottomBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Обеспечивает, что высота будет как минимум высотой экрана */
}

.main-content {
  flex: 1; /* Позволяет основному контенту занимать доступное пространство */
}
</style>
