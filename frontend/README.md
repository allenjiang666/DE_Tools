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

## keep track of the value of a ref after navigating away from the current route and then coming

### 1. Using VueX or Pinia (Global State Management)

### 2. Using localStorage or sessionStorage

- Save to Storage: When the ref value changes, save it to localStorage or sessionStorage.
- Persistence: localStorage persists data even after the browser is closed, whereas sessionStorage keeps the data until the browser tab is closed.

```javascript
import { ref, onMounted, watch } from "vue";

export default {
  setup() {
    const myRef = ref(initialValue);

    // Initialize ref from localStorage
    onMounted(() => {
      const storedValue = localStorage.getItem("myRef");
      if (storedValue !== null) {
        myRef.value = storedValue;
      }
    });

    // Watch for changes and update localStorage
    watch(myRef, (newValue) => {
      localStorage.setItem("myRef", newValue);
    });

    return { myRef };
  },
};
```
