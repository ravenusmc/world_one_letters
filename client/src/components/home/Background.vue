<template>
  <div>

    <section>

      <div class='titleDiv'>
        <h2 class='font'>Background and Reasons for this study</h2>
      </div>

      <div class='reasonDiv'>
        <p class='font'>
          At this point, I've lost count of how many projects I've done on war. I
          have to admit that ever since I've been fascinated with war and once
          I developed some 'decent' coding skills I've made quite a few projects on
          them. This project will not be focusing on death counts but instead will
          be examining letters that were written during World War One. I'll be using
          a basic sentiment analysis tool to accompolish this goal.
        </p>
      </div>

    </section>

  </div>
</template>

<script>
export default {
  name: 'Background',
}
</script>

<style scoped>

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 3em;
  margin-top: 50px;
  margin-bottom: 50px;
}

.titleDiv {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 15%;
  color: #222222;
}

.reasonDiv {
  margin-right: 15%;
  font-size: 18px;
  line-height: 28px;
  color: #222222;
}

/* Media Queries */
@media only all and (max-width: 900px) {

  section {
    grid-template-columns: 1fr;
    grid-gap: .5em;
  }

  .titleDiv {
    margin-left: 10%;
    margin-right: 10%;
  }

  .reasonDiv {
    margin-right: 10%;
    margin-left: 10%;
  }

}
</style>
