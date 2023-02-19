<script setup lang="ts"></script>

<template>
  <nav>
    <div class="content">
      <h4>
        <router-link to="/" class="no-style">
          <img src="/toilet.svg" class="icon" />
          Water Watcher COVID-19
        </router-link>
      </h4>
      <div class="spacer"></div>
      <h4><router-link to="/">Track</router-link></h4>
      <h4><router-link to="/about">About</router-link></h4>
      <h4><router-link to="/notify">Get Notified</router-link></h4>
    </div>
  </nav>
</template>

<style scoped lang="scss">
.icon {
  height: 2rem;
  color: $light;
}

h4 {
  margin: 0;
}

nav {
  padding: 1.5rem;
  font-size: 20px;
  font-weight: bold;
  background-color: $black;

  .content {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 4rem;
    max-width: 960pt;
    margin: 0 auto;
  }
}

.spacer {
  flex: 1;
}

a {
  text-decoration: none;
  color: $light;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
}

a:not(.no-style) {
  border-bottom: 1pt solid transparent;

  &:hover,
  &.router-link-active {
    border-bottom-color: $light;
    color: $lightest;
    opacity: 1;
  }
}
</style>
