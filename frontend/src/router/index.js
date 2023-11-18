import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/realtime",
      name: "realtime",
      component: () => import("../views/RealtimeView.vue"),
    },
    {
      path: "/batch",
      name: "batch",
      component: () => import("../views/BatchView.vue"),
    },
    {
      path: "/online",
      name: "online",
      component: () => import("../views/OnlineView.vue"),
    },
    {
      path: "/offline",
      name: "offline",
      component: () => import("../views/OfflineView.vue"),
    },
    // {
    //   path: "/flows",
    //   name: "Flows",
    //   component: () => import("../components/FlowGrid.vue"),
    // },
    {
      path: "/flows/:id",
      name: "FlowDetail",
      component: () => import("../components/FlowDetail.vue"),
    },
  ],
});

export default router;
