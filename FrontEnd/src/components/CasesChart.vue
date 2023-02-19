<script setup lang="ts">
import getCases from '@/scripts/cases'
import qs from 'qs'
import Chart, { Point } from 'chart.js/auto'
import { format as formatDate } from 'date-fns'
import { onMounted, ref, watch } from 'vue'
import colors from '@/scripts/colors'

const props = defineProps<{ county: string }>()

// const fmtDate = (date: string | Date) => formatDate(new Date(date), 'MMM d, y')
const fmtDate = (date: string | Date) => new Date(date).getTime()

const canvas = ref<null | HTMLCanvasElement>(null)

type WaterTests = {
  [plantId: string]: {
    [date: number]: number
  }
}

type CovidCases = {
  [date: string]: number
}

let chart: Chart
function initChart() {
  if (!canvas.value) throw new Error('Canvas is not defined')
  chart = new Chart(canvas.value, {
    type: 'scatter',
    options: {
      color: colors.medium + (50).toString(16),
      backgroundColor: 'rgba(0,0,0,0)',
      showLine: true,
      borderColor: colors.medium + (50).toString(16),
      scales: {
        y: {
          min: 0,
          max: 100,
        },
        x: {
          ticks: {
            source: 'data',
            // callback: val => formatDate(new Date(val), 'MMM d, y'),
          },
        },
      },
    },
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

  let dates = Object.keys(Object.values(waterTests)[0]).map(a => {
    console.log({ a })
    return new Date(parseInt(a) * 1000)
  })

  // chart.data.labels = dates.map(a => formatDate(a, 'MMM d, y'))

  chart.data.datasets = [
    {
      label: 'Cases per 1m in ' + props.county,
      borderColor: colors.red,
      backgroundColor: colors.red,
      // @ts-ignore
      data: Object.entries(cases)
        .sort((a, b) => a[0] - b[0])
        .map(val => ({
          x: val[0] / 1000,
          y: val[1] * 10,
        })),
    },

    // @ts-ignore
    ...Object.entries(waterTests).map(([plantName, plant]) => ({
      label: 'Waste Water Quality at plant ' + plantName,
      data: Object.entries(plant).map(([date, val]) => {
        console.log(date)
        return {
          x: new Date(parseInt(date)).getTime(),
          y: val,
        }
      }),
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
