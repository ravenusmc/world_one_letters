<template>
  <div>
    <Header/>
    <h1>This is an about page</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/generic/Header.vue'

export default {
  name: 'Home',
  components: {
    Header,
  }
}
</script>
