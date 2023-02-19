<script setup lang="ts">
import qs from 'qs'
import Chart from 'chart.js/auto'
import { format as formatDate } from 'date-fns'
import { onMounted, ref } from 'vue'

const props = defineProps<{ county: string }>()

const canvas = ref<null | HTMLCanvasElement>(null)

type WaterTests = {
  [plantId: string]: {
    [date: string]: number
  }
}

type CovidCases = {
  [date: string]: number
}

const res1 = await fetch('https://localhost:5000/jsonfile?' + qs.stringify({ county: props.county }))
const waterTests: WaterTests = await res1.json()

const res2 = await fetch('/?' + qs.stringify({ county: props.county }))
const covidCases: CovidCases = await res2.json()

function getAllDates() {
  const dates: string[] = []

  for (let i = 0; i < Object.keys(covidCases).length; i++) {
    const date = Object.keys(covidCases)[i]
    if (!(date in dates)) {
      dates.push(date)
    }
  }

  for (let i = 0; i < Object.values(waterTests).length; i++) {
    const plant = Object.values(waterTests)[i]
    for (let j = 0; j < Object.keys(plant).length; j++) {
      const date = Object.keys(plant)[j]
      if (!(date in dates)) {
        dates.push(date)
      }
    }
  }

  return dates.map(a => formatDate(new Date(a), 'MMM d, y'))
}

onMounted(() => {
  if (!canvas.value) throw new Error('Canvas is not defined')

  new Chart(canvas.value, {
    type: 'line',
    data: {
      labels: getAllDates(),
      datasets: [
        // Covid cases

        // Test results for each water treatment plant
        ...Object.entries(waterTests).map(([plantName, plant]) => ({
          label: 'Waste Water Quality at plant ' + plantName,
          data: Object.values(plant),
        })),
      ],
    },
  })
})
</script>

<template>
  <canvas ref="canvas" />
</template>
