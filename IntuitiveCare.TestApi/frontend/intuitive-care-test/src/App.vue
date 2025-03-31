
<template>
  <main class="container d-flex flex-column justify-content-center align-items-center vh-100">
    <span class="fs-1 text-uppercase mb-3 text-secondary">Realizar Pesquisa</span>
    <div class="row mb-5">
      <div class="col-6 p-0">
        <input v-model="searchText" type="search" class="form-control" placeholder="Pesquise aqui...">
      </div>
      <div class="col-4 p-0">
        <select  class="form-select" v-model="optionSelected">
          <option :value="0">ANS</option>
          <option :value="1">CNPJ</option>
        </select>
      </div> 
      <div class="col-2 p-0">
        <button type="button" class="btn btn-primary" @click="onSearchClick">Buscar</button>
      </div> 
    </div>
    <div class="table-responsive">
      <table class="table">
      <thead>
        <tr>
          <td>ANS</td>
          <td>CNPJ</td>
          <td>DATA REGISTRO</td>
          <td>MODALIDADE</td>
          <td>EMAIL</td>
          <td>RAZÃO SOCIAL</td>
        </tr>
      </thead>
      <tbody>
        <template v-for="item in dataSet" >
          <tr>
            <td>{{ item.data.ANS}}</td>
            <td>{{ item.data.CNPJ }}</td>
            <td>{{ item.data.DataRegistro }}</td>
            <td>{{ item.data.Modalidade }}</td>
            <td>{{ item.data.Email }}</td>
            <td>{{ item.data.Modalidade }}</td>
          </tr>
        </template>
      </tbody>
    </table>
    </div>
    
  </main>
  
</template>

<script setup>
import { ref } from 'vue';
import http from '@/services/http.js';
const searchText = ref('')
const optionSelected = ref(0)
const dataSet = ref();

const onSearchClick = async () =>{
  await http.post(`/resources`,{ 
    value: searchText.value,
    typeSearch:  optionSelected.value
  })
  .then(response => {
    dataSet.value = new Array(response);
   
  })
  .catch(err => {
    alert('Erro na consulta, verifique o campo de pesquisa');
  });


 
}

</script>

<style scoped>
</style>
