<script setup lang="ts">
import getCases from '@/scripts/cases'
import qs from 'qs'
import Chart, { Point } from 'chart.js/auto'
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

  const allCases = await getCases()
  console.log({ allCases })
  const cases = allCases[props.county + ' County']

  let dates: string[] = []
  for (let i = 0; i < Object.keys(cases).length; i++) {
    const date = Object.keys(cases)[i]
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
  console.log(dates)

  // FIll missing entries in the cases data
  for (let i = 0; i < dates.length; i++) {
    const date = dates[i]

    let j = i
    while (!cases[date] && j < dates.length) {
      // if (j == dates.length - 1) {
      //   j = 0
      // }
      cases[date] = cases[dates[j]]
      j++
    }

    let k = i
    for (let i = 0; i < Object.keys(waterTests).length; i++) {
      const plant = Object.keys(waterTests)[i]

      while (!waterTests[plant][date] && k < dates.length) {
        waterTests[plant][date] = waterTests[plant][dates[k]] ?? undefined
        k++
      }
    }
  }

  chart.data.labels = dates.map(a => new Date(a).getTime())

  chart.data.datasets = [
    // Covid cases
    {
      label: 'Cases in ' + props.county,
      data: Object.values(cases).map(a => a * 10),
    },

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
