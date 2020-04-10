<template>
  <div>

    <div class='center'>
      <h1 class='font'>The Study</h1>
    </div>

    <section>
      <TimeLine />
    </section>

    <GraphCard
      :type='LineChart'
      :data='sentimentData'
      :options='chartOptionsOne'>
    </GraphCard>

  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/graphCards/GraphCard.vue';
import TimeLine from '@/components/graphCards/TimeLine.vue';

export default {
  name: "Study",
  components: {
    GraphCard,
    TimeLine,
  },
  data() {
  return {
    LineChart: 'LineChart',
    TimeLine: 'Timeline',
    chartOptionsOne: {
        title: 'Sentiment During World War 1',
        legend: { position: 'top' },
        height: 500,
        // vAxis: {
        //   viewWindow: {
        //     max: 0.5,
        //     min: -0.5,
        //   },
        // },
      },// End Chart One Options
    }
  },// End Data area
  computed: {
    ...mapGetters([
      'sentimentData',
      'battleTimeLine',
    ]),
  },
}
</script>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
