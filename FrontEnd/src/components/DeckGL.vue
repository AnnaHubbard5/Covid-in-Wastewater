<script setup lang="ts">
import { Deck } from '@deck.gl/core/typed'
import { GeoJsonLayer, ArcLayer, PolygonLayer } from '@deck.gl/layers/typed'
import { onMounted } from 'vue'

const props = defineProps<{ modelValue: string }>()
const emit = defineEmits(['update:modelValue'])

// source: Natural Earth http://www.naturalearthdata.com/ via geojson.xyz
const CALIFORNIA_COUNTIES = '/data/california-counties-prop.json' //'../public/data/california-counties.json'

const COUNTRIES =
  'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_scale_rank.geojson' //eslint-disable-line
const AIR_PORTS =
  'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_airports.geojson'

const INITIAL_VIEW_STATE = {
  latitude: 36,
  longitude: -120.5,
  zoom: 5.25,
  bearing: 0,
  pitch: 30,
}


function getGradientColor(value: number): Uint8Array{
  if (value == -1)
    return Uint8Array.from([210,105,30, 255])
  var distance = value / 100
  // Calculate the color based on the distance
  if (distance < 0.2) {
    // Green to yellow gradient
    var r = 255;
    var g = Math.floor(255 * (distance / 0.2));
    var b = 0;
  } else if (distance < 0.6) {
    // Yellow to orange gradient
    var r = 255;
    var g = 255;
    var b = Math.floor(255 * ((distance - 0.2) / 0.4));
  } else {
    // Orange to red gradient
    var r = Math.floor(255 * ((distance - 0.6) / 0.4));
    var g = Math.floor(255 * ((distance - 0.6) / 0.4));
    var b = Math.floor(255 * ((distance - 0.6) / 0.4));
  }
  return Uint8Array.from([r, g, b, 255]);
}


// function getGradientColor(value: number): Uint8Array{
//   if (value == -1)
//     return Uint8Array.from([210,105,30, 255])
//   // Calculate the distance from the value to 1
//   var distance = value / 100;

//   // Calculate the color based on the distance
//   if (distance < 0.3) {
//     // Green to yellow gradient
//     var r = 0;
//     var g = 255;
//     var b = 0;
//   } else if (distance < 0.5) {
//     // Yellow to orange gradient
//     var r = 255;
//     var g = Math.floor(255 *  distance);
//     var b = 0;
//   } else {
//     // Orange to red gradient
//     var r = 255;
//     var g = Math.floor(255 *  distance);
//     var b = 0;
//   }

//   return Uint8Array.from([r, g, b, 255]);
// }


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
        getFillColor: [190, 190, 190],
      }),
      new GeoJsonLayer({
        id: 'overlay',
        data: CALIFORNIA_COUNTIES,
        // Styles
        stroked: true,
        filled: true,
        lineWidthMinPixels: 2,
// <<<<<<< Updated upstream
        opacity: 0.1,
        getLineColor: [0, 0, 0],
        getFillColor: [15, 15, 15],
//         getLineColor: [139,0,0],//(d: any) => getGradientColor(d.properties.percentile),
//         // (d: any) => d.properties?.percentile ? getGradientColor(d.properties.percentile) : [0, 0, 0],
//         getFillColor: (d: any) => getGradientColor(d.properties.percentile),
// >>>>>>> Stashed changes
        pickable: true,
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
  <canvas id="deck-canvas" />
</template>
