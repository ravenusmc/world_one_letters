<template>
  <div>

    <nav>

      <div>
        <h3 class='font navTitle'>World War One Letters</h3>
      </div>

      <div class='linkDiv'>
        <router-link class='font routerLinkFormatting' to="/">Home</router-link> |
        <router-link class='font routerLinkFormatting' to="/explore">Explore</router-link> |
        <router-link class='font routerLinkFormatting' to="/about">About</router-link>
      </div>

    </nav>

  </div>
</template>

<script>
export default {
  name: "Nav",
}
</script>

<style scoped>

nav {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.navTitle {
  color: white;
  background-color: rgba(0, 0, 0, 0.2);
  font-size: 30px;
  padding: 10px;
  border-radius: 10px;
}

.linkDiv {
  display: flex;
  flex-direction: row;
  align-items: center;
  font-size: 30px;
}

.routerLinkFormatting {
  color: white;
  text-decoration: none;
  background-color: rgba(0, 0, 0, 0.1);
  padding: 10px;
}

.routerLinkFormatting:hover {
  border-bottom: 2px solid #333;
}

</style>
