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
      <p class="help is-success">Registrēts klients</p>
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
      <button class="button">Registrēt</button>
    </div>
  </form>

  <div class="field">
    <button class="button" @click="showBlock(show)">
      Auto registrācijas forma
    </button>
  </div>
  <div class="block" v-bind:class="{ 'block-show': !show }">
    <div class="field">
      <label class="label">Modelis</label>
      <div class="control">
        <input class="input is-success" type="text" placeholder="Text input" />
      </div>
    </div>
    <div class="field">
      <label class="label">Auto numurs</label>
      <div class="control">
        <input class="input" type="text" placeholder="Text input" />
      </div>
      <p class="help is-success">Registrēts auto numurs</p>
    </div>
    <div class="field">
      <label class="label">VIN numurs</label>
      <div class="control">
        <input class="input" type="text" placeholder="Text input" />
      </div>
      <p class="help is-success">Registrēts auto vin</p>
    </div>
    <div class="field">
      <label class="label">Odometris</label>
      <div class="control">
        <input class="input" type="numbers" placeholder="Nobraukums" />
      </div>
    </div>
    <div class="field">
      <button class="button">Registrēt auto</button>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: "CustomerRegView",
  data() {
    return {
      show: false,
      phone: "",
      customername: "",
    };
  },
  methods: {
    async regcustomer() {
      let payload = { customername: this.customername, phone: this.phone };
      await axios.post("/customer/reg", payload, {
        headers: {
          "Content-type": "application/json",
        },
      }).then((res) => {  
        console.log(res);
      }).catch((error) => {
        console.log(error);
      })
    },
    showBlock(check) {
      this.show = !check;
    },
  },
};
</script>

<style>
.block-show {
  display: none;
}
</style>