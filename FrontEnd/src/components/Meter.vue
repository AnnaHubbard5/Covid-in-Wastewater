<script setup lang="ts">
const props = defineProps<{ val: number; min: number; max: number }>()
</script>

<template>
  <div class="bg">
    <div class="dial" :style="{ '--amount': `${val / (max - min)}` }"></div>
    <div class="center"></div>
    <span>{{ min }}</span>
    <span>{{ max }}</span>
    <span>{{ val }}</span>
  </div>
</template>

<style scoped lang="scss">
.bg {
  position: relative;
  background: conic-gradient(
    from 225deg,
    green 90deg,
    yellow 91deg,
    yellow 180deg,
    red 181deg,
    red 270deg,
    transparent 271deg
  );
  height: 8rem;
  width: 8rem;
  border-radius: 100%;
}

.center {
  background: $bg;
  top: 50%;
  width: 2rem;
  height: 2rem;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  border-radius: 100%;
}

.min,
.max,
.val {
  position: absolute;
}
.min {
  left: 20%;
  top: 80%;
}
.max {
  right: 20%;
  top: 80%;
  text-align: right;
}
.val {
  top: 90%;
  left: 50%;
  text-align: center;
}

.dial {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 0);
  background: red;
  width: 2px;
  height: 50%;
}
</style>
