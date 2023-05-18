<template>
  <h2 class="title">Registrēt klientu</h2>
  <form @submit.prevent="regcustomer" method="POST">
    <div class="field">
      <label class="label">Klienta nosaukums</label>
      <div class="control">
        <input class="input is-success" type="text" placeholder="Vārds Uzvārds vai uzņēmuma nosaukums"
          v-model="customername" />
      </div>
      <p class="help is-success" v-bind:class="{ 'block-show': showProblem }">
        Klients registrēts
      </p>
      <p class="help is-success" v-bind:class="{ 'block-show': showProblemName }">
        Aizpildi klienta nosaukums
      </p>
    </div>
    <div class="field">
      <label class="label">Telefons</label>
      <div class="control">
        <input class="input" type="text" placeholder="2*******" v-model="phone" />
      </div>
      <p class="help is-success" v-bind:class="{ 'block-show': showProblem }">
        Registrēts talrunis
      </p>
      <p class="help is-success" v-bind:class="{ 'block-show': showProblemPhone }">
        Aizpildi talruni
      </p>
    </div>
    <div class="field">
      <label class="label">Klienta veids</label>
      <div class="control">
        <div class="select">
          <select v-model="customer_type">
            <option>Fizisks</option>
            <option>Juridisks</option>
          </select>
        </div>
      </div>
    </div>
    <div class="field">
      <label class="label">Reg. nr. vai Personas kods</label>
      <div class="control">
        <input class="input is-success" type="text" v-model="customer_number" />
      </div>
    </div>
    <div class="field">
      <label class="label">Adrese</label>
      <div class="control">
        <input class="input is-success" type="text" v-model="customer_street" />
      </div>
    </div>
    <div class="field">
            <label class="label">Norēķinu banka</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_bank_name"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Norēķinu konts</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_bank_acc"
              />
            </div>
          </div>
    <div class="field">
      <p class="buttons">
        <button class="button">Registrēt</button>
        <router-link class="button is-primary" v-bind:class="{ 'block-show': showLinkToCustomer }"
          :to="'/dashboard/customers/' + customerid">Klienta lapa</router-link>
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
      customer_type: "",
      customer_number: "",
      customer_street: "",
      customer_bank_name: "",
      customer_bank_acc: "",
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
    async regCustomerType() {

    },
    async regcustomer() {
      if (this.isEmptyFields()) {
        let payload = { customername: this.customername, phone: this.phone };
        let payloadData = {
          customer_type: this.customer_type,
          customer_number: this.customer_number,
          customer_street: this.customer_street,
          customer_bank_name: this.customer_bank_name,
          customer_bank_acc: this.customer_bank_acc,
        };
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