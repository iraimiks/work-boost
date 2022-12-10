<template>
  <router-view />
</template>
<script>

import axios from "axios";

export default {
  name: "App",
  methods: {
    async logout() {
      await axios
        .get("/auth/logout", {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          if (res.data.status === "logout") {
            window.location.href = "/";
          } else {
            console.log("problems");
          }
        });
    },
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
};
</script>
<style lang="scss">
@import "../node_modules/bulma";
</style>