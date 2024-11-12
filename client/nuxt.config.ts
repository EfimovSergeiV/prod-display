// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },

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
      baseURL: 'http://127.0.0.1:8000/',
    },
  },
})
