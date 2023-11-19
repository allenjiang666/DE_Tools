<template>
    <h2 class="p-2 text-2xl font-bold text-center">Create Vintage Json File</h2>
    <form @submit.prevent="handleSubmit">
        <div class="w-full m-2 border border-gray-200 rounded-lg bg-gray-50 ">
            <div class="p-4 ">
                <codemirror v-model="user_input.query" placeholder="TYPE OR PASTE YOUR QUERY ..."
                    :style="{ height: '380px' }" :autofocus="true" :indent-with-tab="true" :tab-size="2"
                    :extensions="extensions" />
            </div>
            <div class="p-3 grid gap-4 md:grid-cols-2">
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-900 ">Bucket</label>
                    <input type="text" id="first_name" v-model="user_input.bucket"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                        placeholder="s3://...." required>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-900">File Name</label>
                    <input type="text" v-model="user_input.file_path"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder=".json" required>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-900">User Email</label>
                    <input type="email" v-model="user_input.email"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder="john.doe@bestegg.com" required>
                </div>
                <div class="w-1/2 flex items-end m-2 p-2">
                    <input type="checkbox" v-model="user_input.download"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 ">
                    <label class="ml-2 text font-medium text-gray-900 0">Download Locally</label>
                </div>
            </div>
            <div class="flex items-center justify-end px-3 py-2 border-t dark:border-gray-600">
                <button type="submit"
                    class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800">
                    Convert
                </button>
            </div>

        </div>
    </form>
</template>
  
<script setup>
import { ref, } from 'vue'
import { Codemirror } from 'vue-codemirror'
import { sql } from '@codemirror/lang-sql'
import axios from 'axios';

const extensions = [sql()]

const user_input = ref({
    query: '',
    email: '',
    bucket: '',
    file_path: '',
    download: false
})


const handleSubmit = async () => {
    try {
        const response = await axios.post('/proxy/8000/convertsql', user_input.value);
        console.log(response);
    } catch (error) {
        console.error(error);
    }
};


</script>