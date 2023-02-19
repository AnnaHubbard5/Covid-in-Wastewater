<script setup lang="ts">
import qs from 'qs'
import Chart from 'chart.js/auto'
import { format as formatDate } from 'date-fns'
import { onMounted, ref, watch } from 'vue'
import colors from '@/scripts/colors'

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

let chart: Chart
function initChart() {
  if (!canvas.value) throw new Error('Canvas is not defined')
  chart = new Chart(canvas.value, {
    type: 'line',
    data: {
      labels: [] as string[],
      datasets: [],
    },
  })
}

async function setData() {
  const res1 = await fetch(
    'http://127.0.0.1:5000/jsonfile?' + qs.stringify({ county: props.county })
  )
  const waterTests: WaterTests = (await res1.json())[props.county]

  let dates: string[] = []
  // for (let i = 0; i < Object.keys(covidCases).length; i++) {
  //   const date = Object.keys(covidCases)[i]
  //   if (!(date in dates)) {
  //     dates.push(date)
  //   }
  // }
  for (let i = 0; i < Object.values(waterTests).length; i++) {
    const plant = Object.values(waterTests)[i]
    for (let j = 0; j < Object.keys(plant).length; j++) {
      const date = Object.keys(plant)[j]
      if (!(date in dates)) {
        dates.push(date)
      }
    }
  }

  dates = dates.map(a => formatDate(new Date(a), 'MMM d, y'))
  chart.data.labels = dates

  chart.data.datasets = [
    // Covid cases

    // Test results for each water treatment plant
    ...Object.entries(waterTests).map(([plantName, plant]) => ({
      label: 'Waste Water Quality at plant ' + plantName,
      data: Object.values(plant),
    })),
  ]

  chart.update()
}

onMounted(() => {
  initChart()
  setData()

  watch(props, setData)
})
</script>

<template>
  <canvas ref="canvas" />
</template>
