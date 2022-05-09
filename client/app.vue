<template>
  <div>
    <Nav/>
    <NuxtPage/>
  </div>
</template>

<script>
 import Book from "@/components/Books.vue"
 import Nav from "@/components/Nav.vue"
 export default {
   components: {
     Book,
     Nav,
   },
   // pages: {
   //   Home,
   // }
 }
</script>

<style scoped>
 .container {
   font-family: Arial, Helvetica, sans-serif;
   color: rgb(27, 60, 138);
   max-width: 50rem;
   margin: 0 auto;
   text-align: center;
 }

</style>
