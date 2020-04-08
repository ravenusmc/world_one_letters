<template>
  <div>
    <GChart
      :type="type"
      :data="data"
      :options="options"
      :resizeDebounce="100" />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'

export default {
  name: 'GraphCard',
  components: {
    GChart
  },
  props: ['type', 'data', 'options'],
};
</script>

<style>
</style>
