<script setup lang="ts">
import CasesChart from '../components/CasesChart.vue'
import DeckGL from '../components/DeckGL.vue'
import { ref, Suspense } from 'vue'

const focusedCounty = ref('')
</script>

<template>
  <div class="container">
    <section>
      <div class="constrain">
        <h1>Current COVID Sewage Levels</h1>
      </div>
      <div class="canvas-container">
        <DeckGL v-model="focusedCounty" />
      </div>
    </section>

    <section v-if="focusedCounty" class="county-data">
      <div class="constrain">
        <h1>History for COVID Content in {{ focusedCounty }} County Sewers</h1>
      </div>
      <Suspense>
        <div class="canvas-container">
          <CasesChart :county="focusedCounty" />
        </div>
      </Suspense>
    </section>
  </div>
</template>

<style scoped lang="scss">
.container {
  padding: 2rem;
}

.canvas-container {
  position: relative;
  height: 70vh;
}
section {
  position: relative;
  text-align: header;
  font-size: $textSize;
  width: 100%;
  max-width: 960pt;
  margin: 0 auto;
}

canvas {
  border: 2px solid $medium;
  border-radius: 0.5rem;
}

h1 {
  text-align: center;
}
</style>
