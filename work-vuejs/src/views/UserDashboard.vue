<template>
  <nav>
    <button @click="logout">Logout</button>
  </nav>
  <div class="home">
    <h2>User page</h2>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UserDashboard",
  methods: {
    async logout() {
      await axios
        .get("/auth/logout", {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          if (res.data.status === 'logout') {
            window.location.href = '/'
          } else {
            console.log('problems')
          }
        });
    },
  },
};
</script>
