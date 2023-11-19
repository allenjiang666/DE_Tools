# Set up vue and fastapi to host on sagemaker instance

There are a few key point for this set up

## vite.config.js

Make sure to set up base in the config

```javascript
base: process.env.NODE_ENV === "production" ? "/proxy/8000/" : "/
```

## Vue router

1. create a const

```javascript
const base = process.env.NODE_ENV === "production" ? "/proxy/
8000/" : "/";
```

2. add this variable to reateWebHistory() function as input:

```javascript
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
});

export default router;
```

## Fix fasapi not serving other routes after mount:

In FastAPI, the order in which routes are declared can affect their accessibility. Ensure that your other routes are declared before mounting the static files. This is because the app.mount call for static files might be catching all requests and trying to serve them as static files, leading to a 404 error for your API routes.
