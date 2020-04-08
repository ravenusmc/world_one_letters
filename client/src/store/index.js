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
    battleTimeLine: [['Battle', 'Date']
    ['Battle of Le Cateau', new Date(1789, 3, 30), new Date(1797, 2, 4)]
    ]
  },

  getters: {
    sentimentData: state => state.sentimentData,
    battleTimeLine: state => state.battleTimeLine,
  },

  actions: {
  },

  mutations: {
  },
})
