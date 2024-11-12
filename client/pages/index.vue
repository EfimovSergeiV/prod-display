<script setup>
  const config = useRuntimeConfig()

  const { data: draws } = await useFetch(`${ config.public.baseURL }d/draw/`)


</script>


<template>
  <div class="flex flex-col justify-between">
    

    <div class="container mx-auto px-4">
      <div class="py-4">
        <p class="text-6xl text-blue-600 font-semibold">Drawing viewer</p>
        <div class="px-1 py-2">
          <p class="text-gray-700">Чертежи к производству</p>
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
        <button @click="removeDraw()" class="w-full bg-red-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl">Удалить </p>
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
