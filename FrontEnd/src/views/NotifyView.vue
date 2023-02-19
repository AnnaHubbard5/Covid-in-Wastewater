<script setup lang="ts">
import qs from 'qs'
import { computed, ref } from 'vue'

const email = ref('')
const county = ref('Select County')
const threshold = ref(60)

const formIsValid = computed(() => {
  return (
    !!email.value.match(/\w+@\w+\.\w+/) &&
    county.value &&
    county.value !== 'Select County' &&
    !!threshold
  )
})

const submit = () => {
  var arg = email.value + "," + county.value + "," + threshold.value;

  var url = "http://127.0.0.1:5000/?arg=" + encodeURIComponent(arg);

  fetch(
    url

      // qs.stringify({
      //   email: email.value,
      //   county: county.value,
      //   threshold: threshold.value,
      // })
  )
  .then(response => response.text())
  .then(data => console.log(data))
  .catch(error => console.error(error));
}

const counties = [
  'Alameda County',
  'Alpine County',
  'Amador County',
  'Butte County',
  'Calaveras County',
  'Colusa County',
  'Contra Costa County',
  'Del Norte County',
  'El Dorado County',
  'Fresno County',
  'Glenn County',
  'Humboldt County',
  'Imperial County',
  'Inyo County',
  'Kern County',
  'Kings County',
  'Lake County',
  'Lassen County',
  'Los Angeles County',
  'Madera County',
  'Marin County',
  'Mariposa County',
  'Mendocino County',
  'Merced County',
  'Modoc County',
  'Mono County',
  'Monterey County',
  'Napa County',
  'Nevada County',
  'Orange County',
  'Placer County',
  'Plumas County',
  'Riverside County',
  'Sacramento County',
  'San Benito County',
  'San Bernardino County',
  'San Diego County',
  'San Francisco County',
  'San Joaquin County',
  'San Luis Obispo County',
  'San Mateo County',
  'Santa Barbara County',
  'Santa Clara County',
  'Santa Cruz County',
  'Shasta County',
  'Sierra County',
  'Siskiyou County',
  'Solano County',
  'Sonoma County',
  'Stanislaus County',
  'Sutter County',
  'Tehama County',
  'Trinity County',
  'Tulare County',
  'Tuolumne County',
  'Ventura County',
  'Yolo County',
  'Yuba County',
]
</script>

<template>
  <div class="constrain">
    <h1>Email Notifications</h1>
    <p>
      Sign up to recieve email notifications when Sewage levels in your area
      exceed a safe threshold.
    </p>
    <div class="form">
      <input type="email" v-model="email" placeholder="Email" />

      <select v-model="county">
        <option value="Select County" disabled selected hidden>County</option>
        <option v-for="c in counties" :value="c">{{ c }}, CA</option>
      </select>

      <label>
        <span>Threshold</span>
        <div class="range">
          <input type="range" v-model="threshold" min="0" max="100" />
          <span class="val">{{ threshold }}%</span>
        </div>
      </label>

      <input
        type="submit"
        value="Submit"
        :disabled="!formIsValid"
        @click="submit"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.constrain {
  max-width: $textWidth;
  margin: 0 auto;
}

.range {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  input {
    flex: 1;
  }
  .val {
    min-width: 4ch;
  }
}

.form {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 1rem;
}

label {
  opacity: 0.7;
}

label,
.form {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
</style>
