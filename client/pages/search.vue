<script setup>

const uploadFiles = (e) => {
  const files = e.target.files || e.dataTransfer.files;
  if (!files.length) return;
  console.log(files);
  // upload(files);
};

</script>


<template>
	<div class="">
		<div class="container mx-auto px-4 py-4 ">
			<p class="">Поиск чертежей</p>			
		</div>



		<div  class="container mx-auto px-4">
			
			<!-- <input 
				v-model="search" 
				type='search'
				id="search-form"
				placeholder="Поиск чертежа"
				class="bg-gray-200 p-2 w-full" 
			>  -->


            <input
              id="newfile" type="file" multiple
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