<script setup>



</script>


<template>
  <div class="flex flex-col justify-between h-screen">
    

    <div class="container mx-auto px-4">
      <div class="py-4">
        <p class="text-6xl text-blue-600 font-semibold">Drawing viewer</p>
      </div>

      
      <div>
        <div class="py-6">
          <p>Чертежи к производству:</p>
        </div>
        
        <PhotoSwipeGallery />
      </div>

    </div>


    <div class="grid grid-cols-3">
      <div class="w-full bg-red-500 flex items-center justify-center py-4">
        <p class="">BUTTON 1</p>
      </div>
      <div class="w-full bg-blue-500 flex items-center justify-center py-4">
        <p class="">BUTTON 2</p>
      </div>
      <div class="w-full bg-green-500 flex items-center justify-center py-4">
        <p class="">BUTTON 3</p>
      </div>
    </div>



  </div>
</template>
