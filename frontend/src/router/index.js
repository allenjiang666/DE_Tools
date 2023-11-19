import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SqlJsonView from "../views/SqlJsonView.vue";
import PinMatchView from "../views/PinMatchView.vue";

const base = process.env.NODE_ENV === "production" ? "/proxy/8000/" : "/";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/sqlToJson",
      name: "sqlToJson",
      component: SqlJsonView,
    },
    {
      path: "/pinMatch",
      name: "pinMatch",
      component: PinMatchView,
    },

    // {
    //   path: "/:id",
    //   name: "Tool",
    //   component: () => import("../components/FlowDetail.vue"),
    // },
  ],
});

export default router;
