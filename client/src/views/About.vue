<template>
  <div>
    <Header/>
    <h1>This is an about page</h1>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/generic/Header.vue'
import Footer from '@/components/generic/Footer.vue';

export default {
  name: 'Home',
  components: {
    Header,
    Footer,
  }
}
</script>
