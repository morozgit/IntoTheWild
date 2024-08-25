import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import ContactPage from '@/views/ContactPage.vue';
import LocationDetail from '@/views/LocationDetail.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/contact', name: 'Contact', component: ContactPage },
  { path: '/location/:id', name: 'LocationDetail', component: LocationDetail }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
