<template>
  <div>

    <section role="region" id='pictureRegion'>

      <div class='imageOne imageSettings'>
      </div>

      <div class='imageTwo imageSettings'>
      </div>

      <div class='imageThree imageSettings'>
      </div>

    </section>

  </div>
</template>

<script>
export default {
  name: "ImageArea",
}
</script>

<style scoped>

#pictureRegion {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 1em;
  margin-left: 3%;
  margin-right: 3%;
  margin-top: 50px;
}

.imageSettings {
  height: 400px;
  background-repeat: no-repeat;
  background-size: 100%;
  border-radius: 15px;
}

.imageOne {
  background-image: url('../../assets/images/imageOne.jpeg');
}

.imageTwo {
  background-image: url('../../assets/images/imageTwo.jpeg');
  height: 240px;
}

.imageThree {
  background-image: url('../../assets/images/imageThree.jpeg');
}

@media only all and (max-width: 900px) {

  #pictureRegion {
    grid-template-columns: 1fr;
    margin-bottom: 50px;
  }

  .imageSettings {
    height: 500px;
    background-size: cover;
  }

  .imageOne {
    background-size: 100%;
    height: 275px;
  }

}

</style>
