<template>
    <h1> Offline Features</h1>
    <FlowGrid flowType="offline" />

    <div class="bg-white p-4 rounded-md shadow">
        <div class="flex items-center justify-between mb-4">
            <h2 class="text-lg font-semibold">View all products</h2>
            <button
                class="flex items-center justify-center px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none">
                <span class="material-icons">add</span>
                Add new product
            </button>
        </div>
        <div class="flex gap-4 mb-4">
            <div class="flex-1">
                <input type="search" placeholder="Search..."
                    class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500" />
            </div>
            <button class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 ">
                Search
            </button>
            <button class="px-4 py-2 text-gray-700 rounded-md border hover:bg-gray-100 focus:outline-none">
                <span class="material-icons">filter_alt</span>
                Filter
            </button>
            <button class="px-4 py-2 text-gray-700 rounded-md hover:bg-gray-100 focus:outline-none">
                <span class="material-icons">settings</span>
                Configurations
            </button>
        </div>
        <div class="flex gap-4 mb-4">
            <label class="flex items-center gap-2">
                <input type="radio" name="productStatus" value="all" class="form-radio" checked />
                All
            </label>
            <label class="flex items-center gap-2">
                <input type="radio" name="productStatus" value="active" class="form-radio" />
                Active products
            </label>
            <label class="flex items-center gap-2">
                <input type="radio" name="productStatus" value="pending" class="form-radio" />
                Pending products
            </label>
            <label class="flex items-center gap-2">
                <input type="radio" name="productStatus" value="inactive" class="form-radio" />
                Inactive products
            </label>
        </div>
        <!-- Additional content goes here -->
    </div>
</template>

<script setup>


import FlowGrid from '../components/FlowGrid.vue';

</script>