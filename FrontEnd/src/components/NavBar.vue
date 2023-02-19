<script setup lang="ts"></script>

<template>
  <nav>
    <div class="spacer"></div>
    <h4><router-link to="/">COVID in Wastewater</router-link></h4>
    <h4><router-link to="/about">About</router-link></h4>
    <h4><router-link to="/notify">Get Notified</router-link></h4>
    <div class="spacer"></div>
  </nav>
</template>

<style scoped lang="scss">
h4 {
  margin: 0;
}

nav {
  display: flex;
  flex-direction: row;
  gap: 4rem;
  padding: 1.5rem;
  font-size: 20px;
  font-weight: bold;
  background-color: $headerbg;
  text-align: center;
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
