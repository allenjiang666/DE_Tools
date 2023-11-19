<template>
    <header class=" bg-white shadow">
        <div class="mx-40">
            <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
                <RouterLink :to="{ name: 'home' }" class="flex items-center">
                    <img src="../asset/de-logo.svg" class="mr-3 h-6 sm:h-9" alt="Logo" />
                    <span class="self-center text-xl text-gray-800 font-semibold whitespace-nowra">DE Tool Box</span>
                </RouterLink>
                <div class="hidden md:flex space-x-8">
                    <form action="#" method="GET" class="hidden lg:block lg:pl-2">
                        <label for="topbar-search" class="sr-only">Search</label>
                        <div class="relative mt-1 lg:w-96">
                            <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                                </svg>
                            </div>
                            <input type="text" id="topbar-search"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full pl-9 p-2.5"
                                placeholder="Search">
                        </div>
                    </form>
                </div>
                <a href="https://marlettefundingllc.atlassian.net/servicedesk/customer/portals"
                    class="text-sm bg-green-500 hover:bg-green-400 text-white py-2 px-4 rounded">Request New
                    Tool</a>
            </nav>
        </div>
    </header>
</template>
  
<script setup>
import { RouterLink } from 'vue-router';
</script>