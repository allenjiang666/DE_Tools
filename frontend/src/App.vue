<script setup>
import { RouterView } from 'vue-router'


import Header from './components/Header.vue';
import SideBar from './components/SideBar.vue';
</script>

<template>
  <div class="antialiased bg-gray-50 dark:bg-gray-900">
    <Header />
    <SideBar />

    <main class="p-5 md:ml-60 h-auto min-h-screen pt-20">
      <RouterView />
    </main>
  </div>
</template>

