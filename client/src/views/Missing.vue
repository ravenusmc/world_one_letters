<template>
  <div>

    <section>
      <div>
        <h1 class='font fontStyle'>Sorry, Page Not Found</h1>
        <router-link class='font fontStyle routerLinkFormatting' to="/">Home</router-link>
      </div>
    </section>

  </div>
</template>

<script>
export default {
}
</script>

<style scoped>

section {
  background-image: url('../assets/images/dogFace.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 1px;
  bottom: 1px; /* Footer Height */
  width: 99%;
}

section div {
  background-color: rgba(0, 0, 0, 0.5);
  padding: 30px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.fontStyle {
  text-transform: uppercase;
  color: white;
}

</style>
