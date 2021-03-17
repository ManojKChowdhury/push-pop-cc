<template>
  <button class="action-button shadow rounded-lg h-8 mr-4 flex justify-between items-center">
    <span class="material-icons text-white ml-4" v-if="icon">{{ icon }}</span>
    <span class="text-white mr-4" v-if="text" :class="{'ml-2':icon,'ml-4':!icon}">{{ text }}</span>
  </button>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      default: ''
    },
    text: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.action-button {
  background-image: linear-gradient(to right top, #ff9232, #fcc34c);

  &:hover {
     -webkit-box-shadow: 0 0 5px 2px rgba(0,0,0,0.27);
     -moz-box-shadow: 0 0 5px 2px rgba(0,0,0,0.27);
     box-shadow: 0 0 5px 2px rgba(0,0,0,0.27);
   }
}
</style>
