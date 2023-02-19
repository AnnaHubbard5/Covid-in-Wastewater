<script setup lang="ts"></script>

<template>
  <nav>
    <div class="spacer">
    <router-link to="/">COVID in Wastewater</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/about">Get Notified</router-link>
    </div>
  </nav>
</template>

<style scoped lang="scss">
nav {
  display: flex;
  flex-direction: row;
  gap: 4rem;
  padding: 1.5rem;
  font-size: 20px;
  font-weight: bold;
  background-color: hsla(0, 4%, 19%, 0.876);
  text-align: center;
}

.spacer {
  flex: 1;
}

a {
  text-decoration: none;
  color: hsl(0, 0%, 100%);
  padding: 1.5rem;

  &:hover {
    border-bottom: 1pt solid;
  }
}
</style>
