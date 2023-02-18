<script setup lang="ts"></script>

<template>
  <nav>
    <div class="spacer"></div>
    <router-link to="/">Covid in Wastewater</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/notify">Get Notified</router-link>
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
  border-bottom: 1pt solid transparent;
  opacity: 0.8;

  &:hover,
  &.router-link-active {
    border-bottom-color: $fg;
    opacity: 1;
  }
}
</style>
