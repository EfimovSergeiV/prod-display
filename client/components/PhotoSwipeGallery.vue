<template>
  <div class="gallery">
    <a
      v-for="(image, index) in images"
      :key="index"
      :href="image.deepZoomSrc"
      :data-pswp-width="image.width"
      :data-pswp-height="image.height"
      :data-deep-zoom="JSON.stringify(image.deepZoomData)"
      class="gallery-item"
    >
      <img :src="image.thumbnail" :alt="`Image ${index + 1}`" />
    </a>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useNuxtApp } from '#app';

// Пример массива изображений с параметрами Deep Zoom
const images = [
  {
    deepZoomSrc: '/WEBP/5 ТМДР.084.083 СБ рама верхняя К-1000 упращенная.webp',
    width: 4961,
    height: 3508,
    thumbnail: '/images/thumb1.jpg',
    deepZoomData: {
      tileSize: 256,
      maxZoomLevel: 20,
      // getTileUrl: (level, x, y) => `/images/tiles/image1/${level}_${x}_${y}.jpg`,
      getTileUrl: 'hallo welt'
    },
  },
  {
    deepZoomSrc: '/WEBP/8ТМДР.120.194 Кронштейн под пневматику.webp',
    width: 2480,
    height: 3508,
    thumbnail: '/images/thumb1.jpg',
    deepZoomData: {
      tileSize: 256,
      maxZoomLevel: 20,
      // getTileUrl: (level, x, y) => `/images/tiles/image1/${level}_${x}_${y}.jpg`,
      getTileUrl: 'hallo welt'
    },
  },
  {
    deepZoomSrc: '/WEBP/8ТМДР.161.309 уголок 2 К-1000.webp',
    width: 4961,
    height: 3508,
    thumbnail: '/images/thumb1.jpg',
    deepZoomData: {
      tileSize: 256,
      maxZoomLevel: 20,
      // getTileUrl: (level, x, y) => `/images/tiles/image1/${level}_${x}_${y}.jpg`,
      getTileUrl: 'hallo welt'
    },
  },

  // {
  //   deepZoomSrc: '/images/large-image2.jpg',
  //   width: 5000,
  //   height: 4000,
  //   thumbnail: '/images/thumb2.jpg',
  //   deepZoomData: {
  //     tileSize: 256,
  //     maxZoomLevel: 5,
  //     getTileUrl: (level, x, y) => `/images/tiles/image2/${level}_${x}_${y}.jpg`,
  //   },
  // },
];

const { $PhotoSwipeLightbox, $PhotoSwipeDeepZoom } = useNuxtApp();

onMounted(() => {
  const lightbox = new $PhotoSwipeLightbox({
    gallery: '.gallery',
    children: 'a',


    // Recommended PhotoSwipe options for this plugin
    allowPanToNext: false, // prevent swiping to the next slide when image is zoomed
    allowMouseDrag: true, // display dragging cursor at max zoom level
    wheelToZoom: true, // enable wheel-based zoom
    zoom: false, // disable default zoom button

    pswpModule: () => import('photoswipe'),
  });

  // Инициализируем Deep Zoom плагин для PhotoSwipe
  new $PhotoSwipeDeepZoom(lightbox, {
    // deep zoom plugin options, for example:
    tileSize: 256
  });

  lightbox.init();
});
</script>


<style scoped>
.gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.gallery-item img {
  width: 150px;
  height: auto;
  cursor: pointer;
  object-fit: cover;
}
</style>
