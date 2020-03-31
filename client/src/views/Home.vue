<template>
  <div>
    <Header/>
    <Background />
    <ImageArea />
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/generic/Header.vue';
import Footer from '@/components/generic/Footer.vue';
import Background from '@/components/home/Background.vue';
import ImageArea from '@/components/home/ImageArea.vue';

export default {
  name: 'Home',
  components: {
    Header,
    Background,
    ImageArea,
    Footer,
  }
}
</script>
