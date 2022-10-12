<template>
  <div>Registrēt klientu</div>
  <form @submit.prevent="regcustomer" method="POST">
    <div class="field">
      <label class="label">Vārds Uzvārds</label>
      <div class="control">
        <input
          class="input is-success"
          type="text"
          placeholder="Vārds Uzvārds"
          v-model="customername"
        />
      </div>
      <p class="help is-success" v-bind:class="{ 'block-show': showProblem }">
        Klients registrēts
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
      <p class="help is-success" v-bind:class="{ 'block-show': showProblem }">
        Registrēts talrunis
      </p>
    </div>
    <div class="field">
      <button class="button">Registrēt</button>
    </div>
  </form>
  <br />
</template>
<script>
import axios from "axios";
export default {
  name: "CustomerRegView",
  data() {
    return {
      showProblem: true,
      phone: "",
      customername: "",
    };
  },
  methods: {
    async regcustomer() {
      let payload = { customername: this.customername, phone: this.phone };
      await axios
        .post("/customer/reg", payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          if (res.data.status === "exist_phone") {
            this.showProblem = false;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.block-show {
  display: none;
}
</style>