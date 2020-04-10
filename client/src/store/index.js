import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    sentimentData: [['Date', 'Sentiment'],
    ['Nov 1914', 0.13131],
    ['Apr 1915', 0.07049],
    ['May 1915', 0.08183],
    ['Jun 1915', -0.00677],
    ['Jul 1915', 0.07356],
    ['Aug 1915', 0.0963],
    ['Sep 1915', 0.08196],
    ['Oct 1915', 0.06556],
    ['Nov 1915', 0.10954],
    ['Dec 1915', 0.06743],
    ['Feb 1916', 0.03015],
    ['Mar 1916', 0.14588],
    ['Apr 1916', 0.09148],
    ['Jun 1916', 0.05594],
    ['Aug 1916', 0.08702],
    ['Jan 1917', 0.12797],
    ['Apr 1917', 0.16397],
    ['Dec 1917', 0.06988],
    ],
    battleTimeLine1914:[
      [
        { type: "string", label: "Battle", id: "Battlee" },
        { type: "date", label: "From", id: "From" },
        { type: "date", label: "To", id: "To" }
      ],
      ['Battle of Le Cateau', new Date(1914, 7, 26), new Date(1914, 7, 27)],
      ['Battle of St. Quentin', new Date(1914, 7, 29), new Date(1914, 7, 30)],
      ['First Battle of the Marne', new Date(1914, 8, 6), new Date(1914, 8, 12)],
      ['First Battle of the Aisne', new Date(1914, 8, 12), new Date(1914, 8, 15)],
      ['First Battle of Ypres', new Date(1914, 9, 19), new Date(1914, 10, 22)],
      ['First Battle of Champagne', new Date(1914, 11, 20), new Date(1915, 2, 17)],
    ],
    battleTimeLine1915:[
      [
        { type: "string", label: "Battle", id: "Battlee" },
        { type: "date", label: "From", id: "From" },
        { type: "date", label: "To", id: "To" }
      ],
      ['Battle of Neuve Chapelle', new Date(1915, 2, 10), new Date(1915, 2, 13)],
      ['Second Battle of Ypres', new Date(1915, 3, 22), new Date(1915, 4, 25)],
      ['Battle of Festubert', new Date(1915, 4, 15), new Date(1915, 4, 27)],
      ['Battle of Loos', new Date(1915, 8, 25), new Date(1915, 8, 28)],
    ],
    battleTimeLine1916:[
      [
        { type: "string", label: "Battle", id: "Battlee" },
        { type: "date", label: "From", id: "From" },
        { type: "date", label: "To", id: "To" }
      ],
      ['Battle of Verdun', new Date(1916, 1, 21), new Date(1916, 11, 18)],
      ['Battle of the Somme', new Date(1916, 6, 1), new Date(1916, 10, 18)],
    ],
    battleTimeLine1917:[
      [
        { type: "string", label: "Battle", id: "Battlee" },
        { type: "date", label: "From", id: "From" },
        { type: "date", label: "To", id: "To" }
      ],
      ['Battle of Arras and Vimy Ridge', new Date(1917, 3, 9), new Date(1917, 3, 12)],
      ['Second Battle of the Aisne', new Date(1917, 3, 16), new Date(1917, 4, 9)],
      ['Battle of Messines', new Date(1917, 5, 7), new Date(1917, 5, 14)],
      ['Third Battle of Ypres - Passchendaele', new Date(1917, 6, 31), new Date(1917, 10, 6)],
      ['Battle of Cambrai', new Date(1917, 10, 20), new Date(1917, 10, 20)],
    ],
    battleTimeLine1918:[
      [
        { type: "string", label: "Battle", id: "Battlee" },
        { type: "date", label: "From", id: "From" },
        { type: "date", label: "To", id: "To" }
      ],
      ['Third Battle of the Aisne', new Date(1918, 4, 27), new Date(1918, 5, 6)],
      ['Battle of Cantigny', new Date(1918, 4, 28), new Date(1918, 4, 28)],
      ['Battles of Chateau Thierry and Belleau Wood', new Date(1918, 5, 3), new Date(1918, 5, 26)],
      ['Second Battle of the Marne', new Date(1918, 6, 15), new Date(1918, 7, 5)],
    ],
  },

  getters: {
    sentimentData: state => state.sentimentData,
    battleTimeLine1914: state => state.battleTimeLine1914,
    battleTimeLine1915: state => state.battleTimeLine1915,
    battleTimeLine1916: state => state.battleTimeLine1916,
    battleTimeLine1917: state => state.battleTimeLine1917,
    battleTimeLine1918: state => state.battleTimeLine1918,
  },

  actions: {

    // This action will get the data for the drill down
    fetchDrillDownData: ({ commit }, { payload }) => {
      console.log({ payload })
      // const path = 'http://localhost:5000/fetchMapData';
      // axios.post(path, payload)
      //   .then((res) => {
      //     commit('setMapData', res.data);
      //   });
    },

  },

  mutations: {
  },
})
