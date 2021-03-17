<template>
  <div class="w-full shadow">
    <div class="flex pl-8 pt-6" v-on:click="showErrors=!showErrors" :class="{'pb-5': !showErrors}">
      <h3 class="text-2xl uppercase">{{ title }}</h3>
      <span class="material-icons large-icon">{{ showErrors? 'keyboard_arrow_up': 'keyboard_arrow_down'}}</span>
    </div>
    <transition name="slide">
      <div class="my-4 h-auto pb-8 bg-gradient-to-r from-indigo-50 to-indigo-100" v-if="showErrors">
        <div v-for="(error, index) in errorList" :key="index" class="w-9/12 h-12 mb-4 ml-8 shadow flex justify-between items-center">
          <span class="ml-4">Code: {{ error.code }}</span>
          <span>{{ error.text }}</span>
          <icon-button v-if="title==='unresolved'" icon="check_circle" text="Mark Resolved"/>
          <icon-button v-if="title==='resolved'" icon="error" text="Mark Unresolved"/>
          <icon-button v-if="title==='backlog'" icon="queue" text="Move to Unresolved"/>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import IconButton from "~/components/IconButton/IconButton";

export default {
  components: {
    IconButton
  },
  props: {
    title: {
      type: String,
      required: true
    },
    errorList: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      showErrors: false
    }
  }
}
</script>

<style lang="scss" scoped>
.large-icon {
  font-size: 2.25rem;
}
</style>
