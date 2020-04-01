<template>
  <div>

    <section>

      <div class='divRectangle'>

        <div class='iconImageOne iconSettings'>
        </div>

        <div class='font font_info'>
          <h5><router-link class='font routerLinkFormatting' to="/explore">Explore</router-link></h5>
        </div>

      </div>

      <div class='divRectangle'>

        <div class='iconImageTwo iconSettings'>
        </div>

        <div class='font font_info'>
          <h5><router-link class='font routerLinkFormatting' to="/about">About</router-link></h5>
        </div>

      </div>

    </section>

  </div>
</template>

<script>
export default {
  name: "Selection"
}
</script>

<style scoped>

section {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 100px;
}

.divRectangle {
  cursor: pointer;
  box-shadow: 5px 10px #888888;
  display: grid;
  grid-template-columns: 45% 45%;
  border: 2px solid black;
  border-radius: 15px;
  width: 20%;
}

.iconSettings {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 100px;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
}

.iconImageOne {
  background-image: url('../../assets/images/iconOne.jpeg');
}

.iconImageTwo {
  background-image: url('../../assets/images/iconTwo.jpeg');
}

.font_info {
  text-transform: uppercase;
  font-size: 20px;
  width: 120%;
  text-align: center;
}

.routerLinkFormatting {
  color: #333;
  text-decoration: none;
}

.routerLinkFormatting:hover {
  border-bottom: 2px solid #333;
}


</style>
