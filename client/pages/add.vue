<script setup>
  const config = useRuntimeConfig()


  const { data: draws } = await useFetch(`${ config.public.baseURL }d/draw/`)


  const uploadFiles = async (event) => {
    console.log(event.target.files)
    /// Отправляем файлы на сервер
    const formData = new FormData()
    for (let i = 0; i < event.target.files.length; i++) {
      formData.append('files', event.target.files[i])
    }
    const response = await fetch(`${config.public.baseURL}d/draw/`, {
      method: 'POST',
      body: formData
    })
    
  }

</script>


<template>
	<div class="">
		<div class="container mx-auto px-4 py-4 ">
			<p class="">Добавить чертежи в очередь</p>			
		</div>



		<div  class="container mx-auto px-4 py-4">
			
			<!-- <input 
				v-model="search" 
				type='search'
				id="search-form"
				placeholder="Поиск чертежа"
				class="bg-gray-200 p-2 w-full" 
			>  -->


      <input id="newfile" type="file" multiple
        class="block w-full text-sm text-slate-500
        file:mr-4 file:py-2 file:px-4
        file:rounded-full file:border-0
        file:text-sm file:font-semibold
        file:bg-sky-700 file:text-white
        hover:file:bg-sky-800 transition-all duration-700"
        @change="uploadFiles"
			/>

		</div>


		<div class="container mx-auto px-4 py-4 ">

      <div class="py-8">
        <p class="text-[8px]">{{ draws }}</p>
      </div>


      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">

        <div class="" v-for="draw in draws" :key="draw.id">
          
          <div class="py-2 flex items-center justify-center">
            <img :src="draw.prw" alt="" class="" />
          </div>
          
          <!-- <img :src="draw.webp" alt="" /> -->
          <div class="py-2 flex items-center justify-center">
            <p class="">{{ draw.name }}</p>
          </div>
          
        </div>

      </div>





		</div>


    <div class=" fixed bottom-0 w-full">
      <div class="grid grid-cols-1 md:grid-cols-3">
        <nuxt-link :to="{ name: 'index' }" class="w-full bg-red-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl">ВЕРНУТЬСЯ</p>
        </nuxt-link>
        <div class="w-full bg-blue-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl"></p>
        </div>
        <button @click="completeDraw()" class="w-full bg-green-500 flex items-center justify-center py-6">
          <p class="text-white font-semibold uppercase text-xl">СОХРАНИТЬ</p>
        </button>
      </div>
    </div>


	</div>


</template>

<style scoped>
	.drop-zone {
		border: 2px dashed #ccc;
		padding: 20px;
		text-align: center;
		transition: background-color 0.3s ease;
	}
	.drop-zone.is-dragover {
		background-color: #f0f0f0;
	}
</style>