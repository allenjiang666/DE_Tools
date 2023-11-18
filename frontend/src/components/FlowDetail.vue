<template>
    <div v-if="loading">Loading...</div>

    <div v-else>
        <h1 class="text-4xl  font-extrabold capitalize">{{ responseData.data.type }} features</h1>

        <!-- Meta Data section -->
        <div class="border my-5 border-gray-200 rounded-lg shadow">
            <div class="bg-gray-200 p-2">
                <h2 class="text-xl font-semibold text-gray-700">Meta Data</h2>
            </div>
            <div class="m-2 p-2 text-gray-700">
                <div class="grid grid-cols-2 gap-4 my-1">
                    <div><strong>Name: </strong>{{ responseData.id }}</div>
                    <div><strong>User: </strong>{{ responseData.data.user }}</div>
                </div>

                <div class="my-1"><strong>Runtime: </strong>{{ responseData.data.lambda.runtime }}</div>
                <div class="my-1"><strong>Layers: </strong>{{ responseData.data.lambda.layers }}</div>
                <div class="my-1"><strong>Features: </strong>{{ responseData.data.features.schema }}</div>
            </div>

        </div>

        <!-- Engineered feature table -->
        <div class="border my-5 border-gray-200 rounded-lg shadow">
            <table class="w-full text-sm text-left text-gray-700 ">
                <thead class="text-xs text-gray-800 bg-gray-200">
                    <tr>
                        <th cope="col" class="p-2 font-bold">Engineered Features</th>
                        <th cope="col" class="p-2 font-bold">Input Features</th>
                        <th cope="col" class="p-2"><span class="sr-only">Edit</span>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(definition, key) in responseData.data.feature_definitons" :key="key"
                        class="bg-white border-b hover:bg-slate-100">
                        <td class="p-2">{{ definition.feature_name }}</td>
                        <td class="p-2">{{ definition.input_features }}</td>
                        <td class="p-2">
                            <FwbButton size="xs" @click="showModal(definition.code)">Definition
                            </FwbButton>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!-- Steps section -->
        <div class="border my-5 border-gray-200 rounded-lg shadow">
            <div class="bg-gray-200 p-2">
                <h2 class="text-xl font-semibold text-gray-700">Pipeline Steps</h2>
            </div>
            <div class="m-2 p-1">
                <div>
                    <ol class="relative m-3 text-gray-500 border-l border-gray-200">
                        <li v-for="(step, key) in responseData.data.steps" :key="key" class="mb-6 ml-6">
                            <button type="button" @click="step.toggle = !step.toggle"
                                :class="{ 'bg-green-200': !step.toggle, 'bg-blue-400': step.toggle }"
                                class="absolute flex items-center justify-center w-8 h-8 bg-green-200 rounded-full -left-4 ring-4 ring-white">
                                <p class="text-green-500">{{ key }}
                                </p>
                            </button>
                            <p type="button" @click="step.toggle = !step.toggle" class="font-medium leading-tight pt-1">
                                {{ step.name }}
                            </p>
                            <pre v-if="step.toggle" v-highlightjs><code class="python"> {{ step.code }}</code></pre>
                        </li>
                    </ol>
                </div>
            </div>
        </div>
    </div>

    <CodeModal v-if="isShowModal" :code="feature_code" @click="isShowModal = false" />
</template>
  
<script setup>
import { FwbButton, } from 'flowbite-vue'
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from "vue-router";
import CodeModal from './CodeModal.vue';


const loading = ref(true);
const responseData = ref(null);

const route = useRoute();
const id = route.params.id;

const isShowModal = ref(false)

const feature_code = ref('')

function showModal(code) {
    isShowModal.value = true
    feature_code.value = code
}



onMounted(() => {
    axios.get(`http://127.0.0.1:8000/items/${id}`)
        .then((response) => {
            if (response.data.data.steps) {
                response.data.data.steps.forEach((obj) => {
                    obj.toggle = false;
                })
            }
            responseData.value = response.data;
            loading.value = false;
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
            loading.value = false;
        });
});



</script>