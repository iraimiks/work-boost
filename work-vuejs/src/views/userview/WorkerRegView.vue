<template>
  <div>Registrēt darbinieku</div>
  <form @submit.prevent="regworker" method="POST">
    <div class="field">
      <label class="label">Vārds</label>
      <div class="control">
        <input
          class="input is-success"
          type="text"
          placeholder="Vārds Uzvārds"
          v-model="name"
        />
      </div>
      <p class="help is-success">Registrēts darbinieks</p>
    </div>
    <div class="field">
      <label class="label">Telefons</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="2*******"
          v-model="phone"
        />
      </div>
      <p class="help is-success">Registrēts talrunis</p>
    </div>
    <div class="field">
      <label class="label">Lietotāj vārds</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="worker-xx"
          v-model="username"
        />
      </div>
      <p class="help is-success">Lietotāja vārds</p>
    </div>
    <div class="field">
      <label class="label">Parole</label>
      <div class="control">
        <input class="input" type="password" v-model="password" />
      </div>
      <p class="help is-success">Parole</p>
    </div>
    <div class="field">
      <button class="button">Registrēt</button>
    </div>
  </form>
  <br />
</template>
<script>
import axios from 'axios'
export default {
  name: "WorkerRegView",
  data() {
    return {
      name: "",
      phone: "",
      username: "",
      password: "",
    };
  },
  methods: {
    async regworker() {
      let payload = {
        name: this.name,
        phone: this.phone,
        username: this.username,
        password: this.password,
      };
      await axios
        .post("/auth/reg_worker", payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>