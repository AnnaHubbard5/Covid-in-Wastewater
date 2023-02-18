<script setup lang="ts"></script>

<template>
  <nav>
    <div class="spacer"></div>
    <router-link to="/">Covid in Wastewater</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/about">Get Notified</router-link>
    <div class="spacer"></div>
  </nav>
</template>

<style scoped lang="scss">
nav {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  padding: 1rem;
}
.spacer {
  flex: 1;
}

a {
  text-decoration: none;
  color: $fg;

  &:hover {
    border-bottom: 1pt solid;
  }
}
</style>
