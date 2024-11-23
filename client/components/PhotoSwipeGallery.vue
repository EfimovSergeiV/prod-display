<script setup>
  import { onMounted } from 'vue';
  import { useNuxtApp } from '#app';

  const config = useRuntimeConfig()
  const props = defineProps(['draws', 'markready']);

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

  const draws = ref(props.draws);

  const removeDraw = async (id) => {
    const formData = new FormData()
    formData.append('id', id)
    const response = await $fetch(`${config.public.baseURL}d/draw/`, {
      method: 'DELETE',
      body: formData
    })

    /// Получаем новый список чертежей
    const newDraws = await $fetch(`${ config.public.baseURL }d/draw/`)
    draws.value = newDraws

  }

</script>


<template>
  <div>
    <div class="gallery grid grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-8">


      <div v-for="(image, index) in draws" class="">

        <transition name="fade" mode="out-in">
          <div v-if="markready" class="absolute z-40">
            <button @click="removeDraw(image.id)" class=" bg-green-500 px-4 py-4">
              <p class="text-center text-white font-bold text-2xl md:text-2xl uppercase">Выполнен</p>
            </button>
          </div>          
        </transition>

        <a
          :key="index"
          :href="image.webp"
          :data-pswp-width="image.webp_size.width"
          :data-pswp-height="image.webp_size.height"
          :data-deep-zoom="JSON.stringify(image.webp)"
          class="gallery-item "
        >

          <div class="bg-white">
            
            <div class="">
              <div class="">
                <img :src="image.prw" :alt="`Image ${index + 1}`" class="w-full" />          
              </div>
            </div>

            <div class="flex items-center justify-center mt-2">
              <p class="text-center text-gray-800">{{ image.name }}</p>
            </div>

          </div>
        </a>


      </div>



    </div>


  </div>

</template>




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