<script setup>
  const config = useRuntimeConfig()

  const { data: draws } = await useFetch(`${ config.public.baseURL }d/draw/`)

  const updateDraw = async () => {
    const newDraws = await $fetch(`${ config.public.baseURL }d/draw/`, {
      method: 'GET'
    })
    draws.value = newDraws
  }


  let intervalId;

  onMounted(() => {
    // Установить интервал каждые 5 минут
    intervalId = setInterval(() => {
      updateDraw()
      // console.log('updateDraw()');
    }, 10000); // 5 минут = 300000 мс
  });

  onUnmounted(() => {
    // Очистить интервал, чтобы избежать утечек памяти
    clearInterval(intervalId);
  });

</script>


<template>
  <div class="flex flex-col justify-between">    

    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between pt-2 pb-8">
        <div class="">
          <nuxt-link :to="{ name: 'index' }">
            <img src="/smlogo.png" alt="logo" class="" />          
          </nuxt-link>
        </div>
        <div class="pl-4">
           <p class="md:text-2xl text-gray-700 font-semibold uppercase">Чертежи к производству</p>
        </div>
      </div>


      <div>
        <div class="mt-4 mb-64 md:mb-24">
          <PhotoSwipeGallery :draws="draws" />
        </div>
      </div>

    </div>


    <div class=" fixed bottom-0 w-full">
      <div class="grid grid-cols-1 md:grid-cols-3">
        <button @click="updateDraw()" class="w-full bg-yellow-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl">Обновить </p>
        </button>
        <nuxt-link :to="{ name: 'add' }" class="w-full bg-blue-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl">Редактировать</p>
        </nuxt-link>
        <button @click="completeDraw()" class="hidden w-full bg-green-500 md:flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl"></p>
        </button>
      </div>
    </div>



  </div>
</template>
