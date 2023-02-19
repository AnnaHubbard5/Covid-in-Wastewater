<script setup lang="ts">
import { Deck } from '@deck.gl/core/typed'
import { GeoJsonLayer, ArcLayer, PolygonLayer } from '@deck.gl/layers/typed'
import { onMounted } from 'vue'

const props = defineProps<{ modelValue: string }>()
const emit = defineEmits(['update:modelValue'])

// source: Natural Earth http://www.naturalearthdata.com/ via geojson.xyz
const CALIFORNIA_COUNTIES = '/data/california-counties.json' //'../public/data/california-counties.json'

const COUNTRIES =
  'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_scale_rank.geojson' //eslint-disable-line


const INITIAL_VIEW_STATE = {
  latitude: 36.5,
  longitude: -120.5,
  zoom: 5.15,
  bearing: 0,
  pitch: 30,
}


function getGradientColor(value: number): Uint8Array{
  if (value == -1)
    return Uint8Array.from([0,0,30, 255])
  var distance = value / 100
  // Calculate the color based on the distance
  if (distance < 0.3) {
    // Green to yellow gradient
    var r = Math.floor(255 * (distance / 4));
    var g = 255;
    var b = 0;
  } else if (distance < 0.45) {
    // Yellow to orange gradient
    var r = Math.floor(255 * distance);
    var g = 244;
    var b = 0;
  } else {
    // Orange to red gradient
    var r = 255;
    var g = Math.floor(255 *  0.4);
    var b = 0;
  }
  return Uint8Array.from([r, g, b, 255]);
}



onMounted(() => {
  const deck = new Deck({
    initialViewState: INITIAL_VIEW_STATE,
    controller: true,
    canvas: 'deck-canvas',
    layers: [
      new GeoJsonLayer({
        id: 'base-map',
        data: COUNTRIES,
        // Styles
        stroked: true,
        filled: true,
        lineWidthMinPixels: 2,
        opacity: 0.4,
        getLineColor: [60, 60, 60],
        getFillColor: [200, 200, 200],
      }),
      new GeoJsonLayer({
        id: 'overlay',
        data: CALIFORNIA_COUNTIES,
        // Styles
        stroked: true,
        filled: true,
        lineWidthMinPixels: 2,
        opacity: 0.3,
        getLineColor: [139,0,0],//(d: any) => getGradientColor(d.properties.percentile),
        // (d: any) => d.properties?.percentile ? getGradientColor(d.properties.percentile) : [0, 0, 0],
        getFillColor: (d: any) => getGradientColor(d.properties.percentile),
        pickable: (d: any) => (d.properties.percentile !== -1),
        autoHighlight: true,
        onClick: info => {
          emit('update:modelValue', info.object.properties.name)
        },
      }),
    ],
  })
})
</script>

<template>
  <canvas id="deck-canvas"/>
</template>
