<template>
  <div>
    <div class="gallery grid grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-8 ">

      <a
        v-for="(image, index) in draws"
        :key="index"
        :href="image.webp"
        :data-pswp-width="image.webp_size.width"
        :data-pswp-height="image.webp_size.height"
        :data-deep-zoom="JSON.stringify(image.webp)"
        class="gallery-item "
      >
        <div class="bg-white">
          
          <div class="">
            <img :src="image.prw" :alt="`Image ${index + 1}`" class="w-full" />          
          </div>

          <div class="flex items-center justify-center mt-2">
            <p class="text-center text-gray-800">{{ image.name }}</p>
          </div>

        </div>
      </a>


    </div>


  </div>

</template>

<script setup>
import { onMounted } from 'vue';
import { useNuxtApp } from '#app';

const props = defineProps(['draws'])

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
  /* display: flex;
  flex-wrap: wrap;
  gap: 20px; */
}

.gallery-item img {
  height: auto;
  cursor: pointer;
  object-fit: cover;
}
</style>