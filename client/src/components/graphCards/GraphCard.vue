<template>
  <div>

    <section id='modalArea' v-if="showModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container">
            <h1>{{ modalTitle }}</h1>

            <div>
              <GraphCard
                :type='Table'
                :data='sentimentData'
                :options='chartOptionsOne'>
              </GraphCard>
            </div>

            <!-- Modal Footer area -->
            <div class="modal-footer">
              <slot name="footer">
                default footer
                <button class="modal-default-button" @click="closeModal()">
                  OK
                </button>
              </slot>
            </div>
            <!-- End Modal Footer area -->

          </div>
        </div>
      </div>
    </section>

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

export default {
  name: 'GraphCard',
  components: {
    GChart,
    GraphCard,
  },
  props: ['type', 'data', 'options'],
  data(){
    return {
      Table: 'Table',
      showModal: false,
      modalTitle: 'Drill Down Data for ',
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
          this.showModal = true
          this.modalTitle = `${this.modalTitle} ${date}`
        }
      }, // End Chart Events
    }
  }, // End of data area
  computed: {
    ...mapGetters([
      'sentimentData',
    ]),
  }, // End Computed Area
  methods: {
    ...mapActions([
      'fetchDrillDownData',
    ]),
    closeModal() {
      this.showModal = false
    }
  }, // End of Methods
};
</script>

<style scoped>

#modalArea {
  border: 2px solid black;
  /* position: fixed; */
  /* z-index: 9998; */
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 600px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

</style>
