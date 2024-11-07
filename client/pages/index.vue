<script setup>



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

        
        <div class="mt-4 mb-24">
          <PhotoSwipeGallery />
        </div>
      </div>

    </div>


    <div class=" fixed bottom-0 w-full">
      <div class="grid grid-cols-3">
        <div class="w-full bg-red-500 flex items-center justify-center py-4">
          <p class="text-white font-semibold">BUTTON 1</p>
        </div>
        <div class="w-full bg-blue-500 flex items-center justify-center py-4">
          <p class="text-white font-semibold">BUTTON 2</p>
        </div>
        <div class="w-full bg-green-500 flex items-center justify-center py-4">
          <p class="text-white font-semibold">BUTTON 3</p>
        </div>
      </div>
    </div>



  </div>
</template>
