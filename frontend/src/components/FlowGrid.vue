<template>
    <div v-if="loading">Loading...</div>
    <div v-else>
        <div class="m-4 grid grid-cols-4 gap-4">
            <div v-for="flow in flowMetaData" :key="flow[0]">
                <RouterLink :to="{ name: 'FlowDetail', params: { id: flow[0] } }"
                    class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 ">
                    <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900">{{ flow[0] }}</h5>
                    <p class="font-normal text-gray-700 text-sm"><strong>User: </strong>{{ flow[1] }}</p>
                    <p class="font-normal text-gray-700 text-sm"><strong>Type : </strong>{{ flow[2] }}</p>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const props = defineProps({
    flowType: String
})

const loading = ref(true);
const flowMetaData = ref(null);

console.log(props.flowType)

onMounted(() => {
    axios.get(`http://127.0.0.1:8000/items/?type=${props.flowType}`)
        .then((response) => {
            console.log(response.data)
            flowMetaData.value = response.data;
            loading.value = false;
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
            loading.value = false;
        });
});

</script>