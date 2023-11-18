<template>
    <FwbModal size="5xl">
        <template #header>
            <div class="flex items-center text-lg font-semibold">
                Feature Definition
            </div>
        </template>
        <template #body>
            <pre v-highlightjs><code class="python"> {{ code }}
            </code></pre>
        </template>
    </FwbModal>
</template>
  
<script setup>

import { FwbModal } from 'flowbite-vue'

const props = defineProps({
    code: String
});


</script>