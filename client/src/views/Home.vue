<template>
  <div>
    <Header
      :class="homeTheme"/>
    <Background />
    <ImageArea />
    <Selection />
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/generic/Header.vue';
import Footer from '@/components/generic/Footer.vue';
import Background from '@/components/home/Background.vue';
import ImageArea from '@/components/home/ImageArea.vue';
import Selection from '@/components/home/Selection.vue';

export default {
  name: 'Home',
  components: {
    Header,
    Background,
    ImageArea,
    Selection,
    Footer,
  },
  data() {
    return {
      homeTheme: 'home-theme',
    }
  },
}
</script>

<style scoped>

.home-theme {
  background-image: url('../assets/images/headerImage.jpg');
  height: 700px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

</style>
