<template>
  <div id="app">

    <h1 class='center font'>Year: {{ this.year }}</h1>

    <form>

      <section>
        <h2 class='font'>Change Year:</h2>
        <div class='upArrow'>
          <i v-on:click="increaseYear()" class="fa fa-arrow-circle-up fa-3x" ></i>
        </div>
        <div>
          <i v-on:click="decreaseYear()" class="fa fa-arrow-circle-down fa-3x"></i>
        </div>
      </section>

    </form>

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
      year: 1914,
      chartData: [],
      chartOptions: {
        width: 800,
        height: 300,
        animation:{
          duration: 1000,
          easing: 'linear',
        },
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
      'battleTimeLine1915',
      'battleTimeLine1916',
      'battleTimeLine1917',
      'battleTimeLine1918',
    ]),
  }, // End Computed Area
  methods: {
    increaseYear() {

      if (this.year >= 1918) {
        alert('Must stay between 1914 and 1918')
      }else {
        this.year += 1
        if (this.year == 1914){
          this.chartData = this.battleTimeLine1914
        }else if (this.year == 1915){
          this.chartData = this.battleTimeLine1915
        }else if (this.year == 1916){
          this.chartData = this.battleTimeLine1916
        }else if (this.year == 1917){
          this.chartData = this.battleTimeLine1917
        }else if (this.year == 1918){
          this.chartData = this.battleTimeLine1918
        }
      }
    }, // End Increase year
    decreaseYear() {
      if (this.year <= 1914) {
        alert('Must stay between 1914 and 1918')
      }else {
        this.year -= 1
        if (this.year == 1914){
          this.chartData = this.battleTimeLine1914
        }else if (this.year == 1915){
          this.chartData = this.battleTimeLine1915
        }else if (this.year == 1916){
          this.chartData = this.battleTimeLine1916
        }else if (this.year == 1917){
          this.chartData = this.battleTimeLine1917
        }else if (this.year == 1918){
          this.chartData = this.battleTimeLine1918
        }
      }
    },// End Decrease year
  },// End Methods
  mounted: function(){
    this.chartData = this.battleTimeLine1914
  }
};
</script>

<style scoped>
section {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  /* margin-bottom: 25px; */
}

.upArrow {
  margin-left: 15px;
  margin-right: 15px;
}
</style>
