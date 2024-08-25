import { createApp } from 'vue';  // Обратите внимание на использование createApp
import App from './App.vue';
import router from './router';
import './main.css'

const app = createApp(App);
app.use(router);
app.mount('#app');
