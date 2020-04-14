<template>
  <div>

      <Modal
        :showModal="showModal"
        :modalTitle="modalTitle"
        @update-number="update"
      />

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
import { mapGetters, mapActions } from 'vuex';
import GraphCard from '@/components/graphCards/GraphCard.vue';
import Modal from '@/components/explore/Modal.vue';

export default {
  name: 'GraphCard',
  components: {
    GChart,
    GraphCard,
    Modal,
  },
  props: ['type', 'data', 'options'],
  data(){
    return {
      Table: 'Table',
      showModal: false,
      modalTitle: 'Drill Down Data for ',
      chartOptionsDrillDown: {
          title: 'Sentiment During World War 1',
          legend: { position: 'top' },
      }, // End Chart One Options
      chartEvents: {
        'select': () => {
          this.modalTitle = 'Drill Down Data for '
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
          this.showModal = true
          this.modalTitle = `${this.modalTitle} ${date}`
        }
      }, // End Chart Events
    }
  }, // End of data area
  computed: {
    ...mapGetters([
      'sentimentData',
      'drillDownData',
    ]),
  }, // End Computed Area
  methods: {
    ...mapActions([
      'fetchDrillDownData',
    ]),
    // closeModal() {
    //   this.showModal = false
    // },
    update(number) {
      this.showModal = number;
    }
    // away: function() {
    //   // this.showModal = false
    //   console.log(this.showModal)
    //   console.log('clicked away');
    // },
  }, // End of Methods
};
</script>

<style scoped>

</style>
