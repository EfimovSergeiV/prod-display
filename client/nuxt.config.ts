// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: false },

  app: {
    head: {
      title: 'DrawingViewer',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/fav.png' }
      ],
    },

    pageTransition: { name: 'page', mode: 'out-in' },

    // pageTransition: {
    //   name: 'fade',
    //   mode: 'out-in' // default
    // },
    // layoutTransition: {
    //   name: 'slide',
    //   mode: 'out-in' // default
    // }
  },

  modules: [
    '@nuxtjs/tailwindcss'
  ],

  plugins: [
    { src: '~/plugins/photoswipe.client.js', mode: 'client' },
    // { src: '~/plugins/navbar.js', mode: 'client' },
  ],

  css: [
    '~/assets/tailwind.css',
    '~/assets/main.css',
    // '@mdi/font/css/materialdesignicons.min.css',
  ],

  runtimeConfig: {
    public: {
      // baseURL: 'http://127.0.0.1:8000/',
      baseURL: 'http://192.168.60.203:8080/',
    },
  },
})
