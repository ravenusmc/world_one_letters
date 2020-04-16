<template>
  <div>

    <section v-if="showLetterModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="font center modal-container">
            <h1>{{ letterDrillDownTitle }}</h1>

            <!-- Modal Body area -->
            <div class='letterArea'>
              <p>{{ letterDrillDownData }}</p>
            </div>
            <!-- End Modal Body area -->

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
import { mapGetters } from 'vuex';
import { GChart } from 'vue-google-charts'

export default {
  name: "LetterModal",
  props: ['showLetterModal', 'letterDrillDownTitle'],
  components: {
    GChart,
  },
  data(){
    return {
      // modalClose: this.showModal,
      Table: 'Table',
      chartOptionsDrillDown: {
          alternatingRowStyle: true,
      }, // End Chart One Options
    }
  },
  computed: {
    ...mapGetters([
      'letterDrillDownData',
    ]),
  }, // End Computed Area
  methods: {
    closeModal() {
      let modalClose = this.showLetterModal;
      modalClose = false
      this.$emit("update-modal", modalClose);
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

.letterArea {
  height: 500px;
  overflow: scroll;
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
