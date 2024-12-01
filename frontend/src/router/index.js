import AllFin from '@/components/AllFin.vue';
import HelloWorld from '@/components/HelloWorld.vue';
import { createRouter, createWebHistory } from 'vue-router';
import 'bootstrap/dist/css/bootstrap.css';
import AddFin from '@/components/AddFin.vue';
import StatisticComponent from '@/components/StatisticComponent.vue';




const routes = [
  
  { path: '/', component: HelloWorld },
  { path: '/allfin', name: 'allfin', component: AllFin },
  { path: '/AddFin', component: AddFin },
  { path: '/StatisticComponent', component: StatisticComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
