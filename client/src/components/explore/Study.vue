<template>
  <div>
    <GraphCard
      :typeOne='typeOne'
      :data='sentimentData'
      :options='chartOptionsOne'>
    </GraphCard>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/graphCards/GraphCard.vue';

export default {
  name: "Study",
  components: {
    GraphCard,
  },
  data() {
  return {
    typeOne: 'LineChart',
    chartOptionsOne: {
        title: 'Sentiment During World War 1',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            max: 0.5,
            min: -0.5,
          },
        },
      },// End Chart One Options
    }
  },// End Data area
  computed: {
  ...mapGetters([
    'sentimentData',
  ]),
},
}
</script>

<style scoped>
</style>
