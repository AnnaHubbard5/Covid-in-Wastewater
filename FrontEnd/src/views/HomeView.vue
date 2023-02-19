<script setup lang="ts">
import CasesChart from '../components/CasesChart.vue'
import DeckGL from '../components/DeckGL.vue'
import { ref, Suspense } from 'vue'

const focusedCounty = ref('')
</script>

<template>
  <section>
    <div class="constrain">
      <h1>Current Data</h1>
    </div>
    <DeckGL v-model="focusedCounty" />
  </section>

  <section v-if="focusedCounty" class="county-data">
    <div class="constrain">
      <h1>History for COVID Content in {{ focusedCounty }} County Sewers</h1>
    </div>
    <Suspense>
      <CasesChart :county="focusedCounty" />
    </Suspense>
  </section>
</template>

<style scoped lang="scss">
section {
  height: 70vh;
  position: relative;
  padding-left: 1.5rem;
  text-align: header;
  font-size: $textSize;
  width: 100%;
  max-width: 960pt;
  margin: 2rem auto;
}

h1 {
  text-align: center;
}

canvas {
  border: 2px solid $medium;
  border-radius: 0.5rem;
}
</style>
