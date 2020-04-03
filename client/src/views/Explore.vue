<template>
  <div>
    <Header
      :class="exploreTheme" />
    <Study/>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/generic/Header.vue';
import Study from '@/components/explore/Study.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'Explore',
  components: {
    Header,
    Study,
    Footer,
  },
  data() {
    return {
      exploreTheme: 'explore-theme',
    }
  },
}
</script>

<style scoped>

.explore-theme {
  background-image: url('../assets/images/exploreHeader.jpg');
  height: 800px;
  width: 100%;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
}


</style>
