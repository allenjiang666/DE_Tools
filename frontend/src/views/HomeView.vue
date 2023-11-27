
<template>
    <h1 class="p-4 text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400">Apps
    </h1>
    <div class="mt-1 p-5 grid grid-cols-4 gap-4">
        <div v-for="tool in tools" :key="tool.id">
            <RouterLink :to="{ name: tool.id }"
                class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-50 hover:transform hover:scale-105 hover:shadow-lg transition-transform duration-300 ease-in-out ">
                <h5>
                    <i class="material-symbols-outlined" :class="tool.color">{{ tool.icon }}</i>
                    <span class="ml-3 text-md font-medium ">{{ tool.name }}</span>
                </h5>

            </RouterLink>
        </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const tools = [
    {
        id: "pinMatch", name: 'PL Pin Match', icon: 'timeline', color: 'text-purple-400',
        description: "This tool is used to prepare PL data to start pin match process"
    },
    {
        id: "sqlToJson", name: 'Create CAS File', icon: 'subject', color: 'text-green-400',
        description: "Convert SQL query result to Json file for CAS Vintage Batch Calculation"
    },
]

</script>
