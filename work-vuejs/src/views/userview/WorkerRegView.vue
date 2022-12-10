<template>
  <h2 class="title">Registrēt darbinieku</h2>
  <form @submit.prevent="regWorker" method="POST">
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
      <p class="help is-success" v-bind:class="{ 'block-show': workerProblem }">
        Registrēts darbinieks
      </p>
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
      <p class="help is-success" v-bind:class="{ 'block-show': phoneProblem }">
        Registrēts talrunis
      </p>
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
      <p
        class="help is-success"
        v-bind:class="{ 'block-show': usernameProblem }"
      >
        Lietotāja vārds
      </p>
    </div>
    <div class="field">
      <label class="label">Parole</label>
      <div class="control">
        <input class="input" type="password" v-model="password" />
      </div>
    </div>
    <div class="field">
      <p class="buttons">
        <button class="button">Registrēt</button>
        <router-link
          class="button is-primary"
          v-bind:class="{ 'block-show': showLinkToWorker }"
          :to="'/dashboard/customers/' + customerid"
          >Klienta lapa</router-link
        >
      </p>
    </div>
  </form>
  <br />
</template>
<script>
import axios from "axios";
export default {
  name: "WorkerRegView",
  data() {
    return {
      name: "",
      phone: "",
      username: "",
      password: "",
      workerid: "",
      workerProblem: true,
      phoneProblem: true,
      usernameProblem: true,
      showLinkToWorker: true,
      worker: true,
    };
  },
  methods: {
    async regWorker() {
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
          if (res.data.status === "exist_worker") {
            this.workerProblem = false;
            this.phoneProblem = false;
            this.usernameProblem = false;
            this.showLinkToWorker = false;
            this.workerid = res.data.worker;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>