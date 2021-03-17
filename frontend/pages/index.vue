<template>
  <div class="container mx-auto h-full w-8/12 max-w-66">
    <error-section v-for="(errorList, errorTitle) in allErrors" :key="errorTitle" :title="errorTitle"
                   :error-list="errorList" class="my-16"/>
    <icon-button text="Undo"/>
    <!--    <notification type="success" message="Error has been moved to resolved."/>-->
  </div>
</template>

<script>
import ErrorSection from "~/components/ErrorSection/ErrorSection";
import IconButton from "~/components/IconButton/IconButton";
/*import Notification from "~/components/Notification/Notification";*/

export default {
  async asyncData({$axios}) {
    try {
      const {resolved, unresolved, backlog} = await $axios.$get("http://localhost:8000/get_lists");
      const allErrors = {
        unresolved,
        resolved,
        backlog
      };
      return {
        allErrors
      };
    } catch (error) {
      console.log(`Couldn't get error lists:\n${error}\nDid you start the API?`);
    }
  },
  components: {
    ErrorSection,
    IconButton,
    /*Notification*/
  },
  data() {
    return {
      allErrors: {
        unresolved: [],
        resolved: [],
        backlog: []
      }
    };
  }
};
</script>
