<script setup lang="ts">
import Meter from '../components/Meter.vue'
</script>

<template>
  <Meter :min="0" :max="10" :val="3" />

<body>
  <div class="about">
  <h1>Why does this matter?</h1>
  <p>
    Three years ago, SCU sent students home from campus with an expected return of two weeks. The return date soon changed to 
    one month and then 6 months and then 1 year. Students were not able to fully return to class in-person until over 1 year 
    after they were sent home. It is clear that COVID is not going away anytime soon and we need to learn how to live with it. 
  </p>
  </div>

  <div class="about">
  <h1>What does Water Watcher COVID-19 do?</h1>
  <p>
    Wastewater plants can now detect for COVID in your waste. With Water Watcher COVID-19, you can sign up for email 
    notifications that notify you of the COVID risk rate in your county.
  </p>
  </div>

  <div class="about">
  <h1>How did we do it?</h1>
  <p>
    We used a dataset from the CDC that includes information about the sample location, date, percentile, and more. We used 
    percentile as the metric to determine risk rate in a given county.
  </p>
  </div>

  <div class="about">
    <p>
      <a href="https://covid.cdc.gov/covid-data-tracker/#wastewater-surveillance" target="_blank"> Learn more</a> about COVID-19 in wastewater
    </p>
  </div>
    
</body>
</template>
