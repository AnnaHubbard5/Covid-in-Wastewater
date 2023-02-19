<script setup lang="ts">
import CasesChart from '../components/CasesChart.vue'
import DeckGL from '../components/DeckGL.vue'
import { ref, Suspense } from 'vue'

const focusedCounty = ref('')
</script>

<template>
  <section>
    <DeckGL v-model="focusedCounty" />
  </section>

  <section v-if="focusedCounty" class="county-data">
    <h1>{{ focusedCounty }}</h1>
    <Suspense>
      <CasesChart :county="focusedCounty" />
    </Suspense>
  </section>
</template>

<style scoped lang="scss">
section {
  height: 80vh;
  position: relative;
}
</style>
