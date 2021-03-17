<template>
  <div :class="notificationClass">
    <span class="ml-4 my-4 text-lg">{{ message }}</span>
    <span class="material-icons mr-4 cursor-pointer">clear</span>
  </div>
</template>

<script>
const NOTIFICATION_CLASSES = {
  'danger': 'bg-red-300',
  'info': 'bg-blue-200',
  'warning': 'bg-yellow-200',
  'success': 'bg-green-200'
};

export default {
  props: {
    type: {
      type: String,
      required: true
    },
    message: {
      type: String,
      required: true
    }
  },
  computed: {
    notificationClass() {
      const classes = "absolute top-0 z-50 h-12 w-8/12 mt-2 flex justify-between items-center rounded-lg shadow-inner";
      return classes + " " + NOTIFICATION_CLASSES[this.type];
    }
  }
}
</script>

<style scoped>

</style>
