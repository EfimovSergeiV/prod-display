<script setup>
  const config = useRuntimeConfig()

  const { data: draws } = await useFetch(`${ config.public.baseURL }d/draw/`)

  const updateDraw = async () => {
    const { data: newDraws } = await useFetch(`${ config.public.baseURL }d/draw/`)
    draws.value = newDraws.value
  }


</script>


<template>
  <div class="flex flex-col justify-between">
    

    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between pt-2 pb-14">
        <div class="">
          <img src="/smlogo.png" alt="logo" class="" />
        </div>
        <div class="">
           <p class="text-2xl text-gray-700 font-semibold uppercase">Чертежи к производству</p>
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
        <button @click="completeDraw()" class="w-full bg-green-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl">Отметить выполненным</p>
        </button>
      </div>
    </div>



  </div>
</template>
