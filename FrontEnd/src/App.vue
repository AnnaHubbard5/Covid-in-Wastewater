<script setup lang="ts">
import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <NavBar />
  <RouterView></RouterView>
</template>

<style lang="scss">
@import "@/assets/main.scss";
</style>
