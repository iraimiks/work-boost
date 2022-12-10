<template>
  <h2 class="title">Registrēt klientu</h2>
  <form @submit.prevent="regcustomer" method="POST">
    <div class="field">
      <label class="label">Klienta nosaukums</label>
      <div class="control">
        <input
          class="input is-success"
          type="text"
          placeholder="Vārds Uzvārds vai uzņēmuma nosaukums"
          v-model="customername"
        />
      </div>
      <p class="help is-success" v-bind:class="{ 'block-show': showProblem }">
        Klients registrēts
      </p>
      <p
        class="help is-success"
        v-bind:class="{ 'block-show': showProblemName }"
      >
        Aizpildi klienta nosaukums
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
      <p
        class="help is-success"
        v-bind:class="{ 'block-show': showProblemPhone }"
      >
        Aizpildi talruni
      </p>
    </div>
    <div class="field">
      <p class="buttons">
        <button class="button">Registrēt</button>
        <router-link
          class="button is-primary"
          v-bind:class="{ 'block-show': showLinkToCustomer }"
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
  name: "CustomerRegView",
  data() {
    return {
      showProblem: true,
      showLinkToCustomer: true,
      customerid: "",
      phone: "",
      customername: "",
      showProblemName: true,
      showProblemPhone: true,
    };
  },
  methods: {
    isEmptyFields() {
      if (this.customername === "") {
        this.showProblemName = false;
        return false;
      } else if (this.phone === "") {
        this.showProblemPhone = false;
        return false;
      } else {
        this.showProblemName = true;
        this.showProblemPhone = true;
        return true;
      }
    },

    async regcustomer() {
      console.log(this.customername);
      console.log(this.phone);
      console.log(this.isEmptyFields());
      if (this.isEmptyFields()) {
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
              this.showLinkToCustomer = false;
              this.customerid = res.data.customer_id;
            } else {
              window.location.href = "/dashboard/customers/" + res.data.redid;
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style>
.block-show {
  display: none;
}
</style>