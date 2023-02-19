<script setup lang="ts">
const props = defineProps<{ val: number; min: number; max: number }>()
</script>

<template>
  <div class="bg">
    <div class="center"></div>
    <div class="dial" :style="{ '--angle': `${val / max * 360 + 225}deg` }"></div>
    <span class="min">{{ min }}</span>
    <span class="max">{{ max }}</span>
    <span class="val">{{ val }}</span>
  </div>
</template>

<style scoped lang="scss">
.bg {
  position: relative;
  background: conic-gradient(
    from 225deg,
    #A3BE8C 90deg,
    #EBCB8B 91deg,
    #EBCB8B 180deg,
    #BF616A 181deg,
    #BF616A 270deg,
    transparent 271deg
  );
  height: 8rem;
  width: 8rem;
  border-radius: 100%;
}

.center {
  background: $darker;
  top: 50%;
  width: 4rem;
  height: 4rem;
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
  left: 50%;
  transform-origin: bottom center;
  transform: rotate(var(--angle));
  background: red;
  width: 2px;
  height: 50%;
}
</style>
