<template>
    <h2 class="p-2 text-2xl font-bold text-center">PL Pin Match </h2>
    <form @submit.prevent="handleSubmit">
        <div class="w-full m-2 border border-gray-200 rounded-lg bg-gray-50 ">
            <div class="p-3 grid gap-4 md:grid-cols-2">
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-600 ">App year </label>
                    <select id="countries" v-model="params.year"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 hover:cursor-pointer">
                        <option v-for="num in Array.from({ length: 11 }, (_, i) => 2023 - i)" :value="num">{{ num }}
                        </option>
                    </select>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-600 ">App month </label>
                    <select id="countries" v-model="params.month"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  hover:cursor-pointer">
                        <option v-for="num in Array.from({ length: 11 }, (_, i) => 11 - i)" :value="num">{{ num }}</option>

                    </select>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-600 ">Staging Database </label>
                    <input type="text" v-model="params.db"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder="BE_SCRATCH" required>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-600 ">Staging Schema</label>
                    <input type="text" v-model="params.schm"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder="DJOHN" required>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-600 ">Staging S3 Bucket</label>
                    <input type="text" v-model="params.s3"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        required>
                </div>
                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-600 ">Staging S3 Prefix</label>
                    <input type="text" v-model="params.prefix"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        required>
                </div>

                <div>
                    <label class="block mb-2 text-sm font-medium text-rose-600">Username</label>
                    <input type="text" v-model="params.USER"
                        class="bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        required>
                </div>


            </div>
            <div class="flex items-center justify-between px-3 py-2 ">

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
                <div v-if="message" class="text-red-600">
                    <span>{{ message }}</span>
                    <button type="button" class="m-1 px-1 rounded-md text-blue-700" @click="showIframe"> show
                        status</button>
                </div>
            </div>
        </div>
    </form>
    <div>

        <iframe v-if="isVisible" :src="iframe_url" class="w-full min-h-screen" frameborder="1"></iframe>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios'

// Form inputs
const params = ref({
    USER: "Elly",
    year: "",
    month: "",
    db: "BE_SCRATCH",
    schm: "EARABMAKKI",
    s3: "mf-datascience",
    prefix: "ascend_pin_matching/transfer_data/new",

})
const submitButton = ref({
    label: "Start Process",
    isLoading: false
});

const iframe_url = ref('')
const handleSubmit = async () => {

    const url = process.env.NODE_ENV === "production" ? "/proxy/8000/pinmatch" : "http://127.0.0.1:8000/pinmatch"

    submitButton.value.isLoading = true;
    submitButton.value.label = 'Loading...';

    try {
        const response = await axios.post(url, params.value);
        message.value = response.data.message
        iframe_url.value = response.data.flow_status_link
    }
    catch (error) {
        message.value = error
        console.error(error);
    }
    finally {
        // Change the label back to 'Download' after the fetch completes
        submitButton.value.isLoading = false;
        submitButton.value.label = 'Start Process';
    }
}

// track flow status

const isVisible = ref(false)
const showIframe = () => isVisible.value = !isVisible.value

//  Track request response
const message = ref('')

</script>
