<template>
  <div>
    <section v-on-clickaway="away" id='clickaway' v-if="showModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="font center modal-container">
            <h1>{{ modalTitle }}</h1>

            <div>
              <GChart
                :type="Table"
                :data="drillDownData"
                :options="chartOptionsDrillDown"
                />
            </div>

            <!-- Modal Footer area -->
            <div class="modal-footer">
              <slot name="footer">
                <button class="font modal-default-button" @click="closeModal()">
                  Close
                </button>
              </slot>
            </div>
            <!-- End Modal Footer area -->

          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mixin as clickaway } from 'vue-clickaway';
import { mapGetters } from 'vuex';
import { GChart } from 'vue-google-charts'

export default {
  name: "Modal",
  mixins: [ clickaway ],
  props: ['showModal', 'modalTitle'],
  components: {
    GChart,
  },
  data(){
    return {
      // modalClose: this.showModal,
      Table: 'Table',
      chartOptionsDrillDown: {
          title: 'Sentiment During World War 1',
          legend: { position: 'top' },
          alternatingRowStyle: true,
      }, // End Chart One Options
    }
  },
  computed: {
    ...mapGetters([
      'drillDownData',
    ]),
  }, // End Computed Area
  methods: {
    closeModal() {
      let modalClose = this.showModal;
      modalClose = false
      this.$emit("update-number", modalClose);
    },
    // This method is for use on vue click away
    away: function() {
      console.log(this.showModal)
      console.log('clicked away');
    },
  }, // End Methods
}
</script>

<style>
#clickaway {
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

.modal-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

button {
  padding: 12px;
  background-color: #333;
  color: white;
  border: 2px solid #333;
  border-radius: 12px;
  text-transform: uppercase;
}
</style>
