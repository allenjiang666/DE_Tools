<template>
  <aside
    class="fixed top-0 left-0 z-40 w-56 h-screen pt-14 transition-transform -translate-x-full bg-white border-r border-gray-200 md:translate-x-0 dark:bg-gray-800 dark:border-gray-700"
    aria-label="Sidenav" id="drawer-navigation">
    <div class="overflow-y-auto py-5 px-3 h-full bg-gray-100 dark:bg-gray-800">

      <!-- Overview -->
      <RouterLink :to="{ name: 'home' }"
        class="flex items-center p-3 w-full text-base font-bold text-gray-900 rounded-lg transition duration-75 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
        <i class="material-symbols-outlined mr-1 text-green-400">dashboard</i>
        <span class="ml-3 ">Overview</span>
      </RouterLink>


      <!-- On Demand -->
      <button type="button"
        class="flex items-center p-3 mt-4 w-full text-base font-normal text-gray-900 rounded-lg transition duration-75 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
        @click="toggleOnDemandDropdown">
        <i class="material-symbols-outlined mr-2 font text-teal-400">air</i>
        <span class="flex-1 ml-3 text-left font-semibold whitespace-nowrap">On Demand</span>
        <i class="material-symbols-outlined text-2xl">expand_more</i>
      </button>
      <ul v-if="isOpenOnDemand" class="space-y-2">
        <li v-for="item in onDemand" :key="item.name">
          <RouterLink :to="{ name: item.href }"
            class="flex justify-start items-center p-2 text-base  text-gray-900 rounded-lg dark:text-white hover:bg-white dark:hover:bg-gray-700 group">
            <i class="material-symbols-outlined mr-1 ml-4" :class="item.color">{{ item.icon }}</i>
            <span class="ml-3 ">{{ item.name }}</span>

          </RouterLink>
        </li>
      </ul>

      <!-- preCalculated -->
      <button type="button"
        class="flex items-center p-3 mt-4 w-full text-base font-normal text-gray-900 rounded-lg transition duration-75 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
        @click="togglePreCalcuateDropdown">
        <i class="material-symbols-outlined mr-2 text-red-400">table</i>
        <span class="flex-1 ml-3 font-semibold text-left whitespace-nowrap">Pre-Calculate</span>
        <i class="material-symbols-outlined text-2xl">expand_more</i>
      </button>
      <ul v-if="isOpenPreCalcuate" class="space-y-2">
        <li v-for="item in preCalculate" :key="item.name">
          <RouterLink :to="{ name: item.href }"
            class="flex justify-start items-center p-2 text-base  text-gray-900 rounded-lg dark:text-white hover:bg-white dark:hover:bg-gray-700 group">
            <i class="material-symbols-outlined mr-1 ml-4" :class="item.color">{{ item.icon }}</i>
            <span class="ml-3 ">{{ item.name }}</span>
          </RouterLink>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router'

const isOpenOnDemand = ref(false)

function toggleOnDemandDropdown() {
  isOpenOnDemand.value = !isOpenOnDemand.value
}

const onDemand = [
  { name: 'Realtime', href: 'realtime', icon: 'timeline', color: 'text-purple-400', current: true },
  { name: 'Batch', href: 'batch', icon: 'subject', color: 'text-green-400', current: false },
]


const isOpenPreCalcuate = ref(false)

function togglePreCalcuateDropdown() {
  isOpenPreCalcuate.value = !isOpenPreCalcuate.value
}

const preCalculate = [
  { name: 'Offline', href: 'offline', icon: 'model_training', color: 'text-pink-400', current: false },
  { name: 'Online', href: 'online', icon: 'dashboard', color: 'text-blue-400', current: false },
]

</script>