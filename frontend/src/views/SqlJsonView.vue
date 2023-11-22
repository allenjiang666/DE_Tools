<template>
    <h2 class="p-2 text-2xl font-bold text-center">Create Vintage File</h2>
    <form @submit.prevent="handleSubmit">
        <div class="w-full m-2 border border-gray-200 rounded-lg bg-gray-50 ">
            <div class="p-4 ">
                <codemirror v-model="user_input.query" placeholder="TYPE OR PASTE YOUR QUERY ..."
                    :style="{ height: '380px' }" :autofocus="true" :indent-with-tab="true" :tab-size="2"
                    :extensions="extensions" />
                <p class="text-gray-500 text-xs pt-1"> Make sure your query only returns <span class="text-red-500">ID
                    </span> and <span class="text-red-500">Date</span> columns</p>
            </div>

            <div class="p-3 grid gap-4 md:grid-cols-2">
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-900 ">Output Bucket </label>
                    <input type="text" id="first_name" v-model="user_input.bucket"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                        placeholder="my-s3-bucket" required>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-900">File Name</label>
                    <input type="text" v-model="user_input.file_path"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder=".csv OR .json" required>
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
                    <label class="ml-2 text font-medium text-gray-900 0">Download</label>
                </div>
            </div>
            <div class="flex items-center justify-between px-3 py-2 border-t dark:border-gray-600">
                <div class="text-red-600">{{ message }}</div>
                <button :disabled="submitButton.isLoading" type="submit"
                    class="m-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 inline-flex items-center">

                    <svg v-if="submitButton.isLoading" aria-hidden="true" role="status"
                        class="inline w-4 h-4 me-3 text-white animate-spin" viewBox="0 0 100 101" fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="#E5E7EB" />
                        <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentColor" />
                    </svg> <span>{{ submitButton.label }}</span>

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
    bucket: 'prd-customer-attribute-service-batches',
    file_path: '',
    download: false
})

const submitButton = ref({
    label: "Generate",
    isLoading: false
});

const message = ref('')

function downloadData(data, fileType) {
    // Convert the data to a JSON blob
    if (fileType === 'json') {
        const Blob = new Blob([JSON.stringify(data)], { type: 'application/json' });
    }
    else {
        const Blob = new Blob([JSON.stringify(data)], { type: 'text/csv' });
    }

    // Create a temporary link for downloading the file
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(jsonBlob);
    downloadLink.download = user_input.value.file_path; // Name of the file

    // Append the link to the document, trigger it, and then remove it
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

const handleSubmit = async () => {
    submitButton.value.isLoading = true;
    submitButton.value.label = 'Loading...';
    try {
        const url = process.env.NODE_ENV === "production" ? "/proxy/8000/convertsql" : "http://127.0.0.1:8000/convertsql"
        const response = await axios.post(url, user_input.value);

        message.value = response.data.message
        const fileType = response.data.file_type

        if (user_input.value.download) {
            downloadData(response.data.json_data, fileType)
        }
    } catch (error) {
        message.value = error
        console.error(error);
    } finally {
        // Change the label back to 'Download' after the fetch completes
        submitButton.value.isLoading = false;
        submitButton.value.label = 'Generate';
    }
};


</script>