<template>
  <section class="hero is-large is-info">
    <div class="hero-body">
      <div class="container is-max-desktop">
        <div class="notification is-info">
          <div class="columns is-centered">
            <div class="column is-half">
              <form @submit.prevent="loginreq" method="POST">
                <div class="field">
                  <label class="label">Lietotājs</label>
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="liet-xxxx"
                      v-model="username"
                    />
                  </div>
                </div>
                <div class="field">
                  <label class="label">Parole</label>
                  <div class="control">
                    <input
                      class="input"
                      type="password"
                      placeholder="Jūsu parole"
                      v-model="password"
                    />
                  </div>
                </div>
                <div class="field">
                  <button class="button">Ienākt</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  mounted() {},
  methods: {
    async loginreq() {
      let payload = { username: this.username, password: this.password };
      await axios.post("/auth/login", payload, {
        headers: {
          "Content-type": "application/json",
        },
      }).then((res) => {
        if (res.data.status === 'logined') {
          window.location.href = '/user/' + res.data.id
        } else {
          console.log('problems');
        }
      }).catch((error) => 
        {
          console.log(error);
        }
      );
    },
  },
};
</script>