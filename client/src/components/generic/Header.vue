<template>
  <div>
    <header>

      <Nav />

    </header>
    <router-view/>
  </div>
</template>

<script>
import Nav from '@/components/generic/Nav.vue';

export default {
  name: "Header",
  components: {
    Nav,
  }
}
</script>

<style scoped>

header {
  background-image: url('../../assets/images/headerImage.jpg');
  height: 700px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

</style>
