<template>
  <div id="app">

    <form @submit="submitForm">
      <button>Submit</button>
    </form>

    <h1>1914</h1>
    
    <GChart
      :settings="{ packages: ['timeline'] }"
      type="Timeline"
      :data="chartData"
      :options="chartOptions"
      :events="chartEvents"
      ref="gChart"
      :resizeDebounce="100"
    />
  </div>
</template>
<script>
import { GChart } from "vue-google-charts";
import { mapGetters } from 'vuex';

export default {
  name: "TimeLine",
  components: {
    GChart
  },
  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        [
          { type: "string", label: "Battle", id: "Battlee" },
          { type: "date", label: "From", id: "From" },
          { type: "date", label: "To", id: "To" }
        ],
        ['Battle of Le Cateau', new Date(1914, 7, 26), new Date(1914, 7, 27)],
        ['First Battle of the Marne', new Date(1914, 8, 6), new Date(1914, 8, 12)],
        ['First Battle of Champagne', new Date(1914, 11, 20), new Date(1915, 2, 17)],
        ['Second Battle of Ypres', new Date(1915, 3, 22), new Date(1915, 4, 25)],
        ['Second Battle of Artois', new Date(1915, 4, 9), new Date(1915, 5, 18)],

      ],
      chartOptions: {
        width: 800,
        height: 500,
      },
      chartEvents: {
        select: () => {
          const table = this.$refs.gChart.chartObject;
          const selection = table.getSelection();
          const onSelectionMeaasge = selection.length !== 0 ? 'row was selected' : 'row was diselected'
          alert(onSelectionMeaasge);
        }
      }
    };
  }, // End Data Area
  computed: {
    ...mapGetters([
      'battleTimeLine1914',
    ]),
  }, // End Computed Area
  methods: {
    submitForm(evt) {
      evt.preventDefault();
      console.log('HDJJD')
      this.chartData = this.battleTimeLine1914
      // this.fetchMapData({ payload });
    },
  },// End Methods
};
</script>
