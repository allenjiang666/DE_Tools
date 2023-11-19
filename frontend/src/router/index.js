import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const base = process.env.NODE_ENV === "production" ? "/proxy/8000/" : "/";

const router = createRouter({
  history: createWebHistory(base),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/sqlToJson",
      name: "sqlToJson",
      component: () => import("../views/SqlJsonView.vue"),
    },
    {
      path: "/pinMatch",
      name: "pinMatch",
      component: () => import("../views/PinMatchView.vue"),
    },

    // {
    //   path: "/:id",
    //   name: "Tool",
    //   component: () => import("../components/FlowDetail.vue"),
    // },
  ],
});

export default router;
