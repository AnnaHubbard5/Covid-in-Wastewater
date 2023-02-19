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
    notifications that notify you of the COVID risk rate in your county. We also created an interactive website. Users can 
    select a county from a map. A graph is then presented below the map with information about the COVID levels based on all 
    of the wastewater treatment plants in the county.
  </p>
  </div>

  <div class="about">
  <h1>How we did it</h1>
  <p>
    We used a dataset from the CDC that includes information about the sample location, sample collection date, COVID level 
    percentile, and more. Using this, we created a map that colors counties based on high, medium, or low COVID levels.
  </p>
  <p>
    To create the email notification, we used a combination of google-cloud API and HTML. Together, we were able to create a 
    message that shares information about the COVID levels in the user's county and guidelines recommended by the CDC.
  </p>
  </div>

  <div class="about">
    <h1> What we learned</h1>
      <p>
        We were most surprised to learn that COVID-19 can be detected from wastewater. We also learned a lot about working 
        with github, as this what we used to create and code our project. Some other new skills we gained include flask, 
        hosting servers, and DeckGL.
      </p>
  </div>

  <div class="about">
    <h1> What's next?</h1>
      <p>
        Our current version only contains data for the counties in California. We plan to expand this dataset to include the 
        rest of the United States and even other countries, if the proper data exists.
      </p>
  </div>

  <div class="about">
    <p>
      <a href="https://covid.cdc.gov/covid-data-tracker/#wastewater-surveillance" target="_blank"> Learn more</a> about COVID-19 in wastewater
    </p>
  </div>
    
</body>
</template>
