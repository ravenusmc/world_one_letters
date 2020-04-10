<template>
  <div>
    <GChart
      :type="type"
      :data="data"
      :options="options"
      :events="chartEvents"
      ref="gChart"
      :resizeDebounce="100" />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import { mapActions } from 'vuex';

export default {
  name: 'GraphCard',
  components: {
    GChart
  },
  props: ['type', 'data', 'options'],
  data(){
    return {
      chartEvents: {
        'select': () => {
          // console.log(this.data) // This will show you the data
          const chart = this.$refs.gChart.chartObject;
          const selection = chart.getSelection()[0];
          // I need to add one to the row because the first row contains the
          // column headers.
          let row = selection.row + 1
          // This pulls out the specific date from the element that the user
          // clicked on
          let date = this.data[row][0]

          const payload = {
            date,
          };

          this.fetchDrillDownData({ payload })

        }
      }, // End Chart Events
    }
  }, // End of data area
  methods: {
    ...mapActions([
      'fetchDrillDownData',
    ]),
  }, // End of Methods
};
</script>

<style>
</style>
