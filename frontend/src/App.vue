<script setup>
import { RouterView } from 'vue-router'

import Header from './components/Header.vue';

</script>

<template>
  <div class="bg-gray-50">
    <Header />
    <main class="mx-40 mt-2 px-5 h-auto min-h-screen bg-white">
      <RouterView />
    </main>
  </div>
</template>

