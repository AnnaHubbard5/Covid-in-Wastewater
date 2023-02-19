<script setup lang="ts">
import { Deck } from '@deck.gl/core/typed'
import { GeoJsonLayer, ArcLayer, PolygonLayer } from '@deck.gl/layers/typed'
import { onMounted } from 'vue';

// source: Natural Earth http://www.naturalearthdata.com/ via geojson.xyz
const CALIFORNIA_COUNTIES = '/data/california-counties.json' //'../public/data/california-counties.json'

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

onMounted(() => {
  const deck = new Deck({
    initialViewState: INITIAL_VIEW_STATE,
    controller: true,
    canvas: "deck-canvas",
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
        opacity: 0.1,
        getLineColor: [139, 0, 0],
        getFillColor: [139, 0, 0],
        pickable: true,
        autoHighlight: true,
        onClick: info =>
          // eslint-disable-next-line
          info.object &&
          alert(
            `${info.object.properties.name}`
          ),
      })   
    ],
  })
})
</script>

<template>
  <canvas id="deck-canvas"></canvas>
</template>
