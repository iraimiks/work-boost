<template>
  <div class="card">
    <div class="card-content">
      <p class="subtitle">Pasūtījuma sagataves forma</p>
    </div>
  </div>
  <div class="columns">
    <div class="column is-8">
      <h3 class="is-size-4 has-text-left">
        Izrakstīšanas datums: <strong>{{ convertDate() }}</strong> (DD.MM.GGGG.)
      </h3>
    </div>
    <div class="column is-8">
      <h3 class="is-size-4 has-text-left">Rēķins Nr. <strong>XXX</strong></h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Preču nosūtītājs: <strong>AUTOBOOST SIA</strong>
      </h3>
    </div>
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        <strong>LV40203418867</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Adrese: <strong>Liepājas iela 5 Ludza</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Norēķinu rekvizīti: <strong>Citadele banka</strong>
      </h3>
    </div>
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        <strong>LV47PARXO027844410001</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Pakalpojuma saņēmējs: <strong>{{ customer.customer_name }}</strong>
      </h3>
    </div>
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Reg. nr.: <strong><input /></strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Addrese: <strong><input /></strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-8">
      <h3 class="is-size-4 has-text-left">
        Pakalpojuma saņemšanas vieta: <strong>Liepājas iela 5 Ludza</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-8">
      <h3 class="is-size-4 has-text-left">
        Apmaksas veids un kārtība:
        <div class="select is-small">
          <select>
            <option>Pārskaitījums</option>
            <option>Ar karti</option>
          </select>
        </div>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Auto: <strong>{{ customer.brand }} {{ customer.number }}</strong>
      </h3>
    </div>
  </div>
  <h2>Detaļu saraksts</h2>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>ID</th>
        <th>Detaļas nosaukums</th>
        <th>Detaļas skaits</th>
        <th>Vienas vienības cena</th>
        <th>Pilnā cena</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in partscar" v-bind:key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.part_name }}</td>
        <td>{{ item.part_count }}</td>
        <td>{{ item.part_price }}</td>
        <td>{{ item.full_price }}</td>
      </tr>
    </tbody>
  </table>
  <h2>Izdarītā darba saraksts</h2>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Darba veids</th>
        <th>Darba apraksts</th>
        <th>Cena</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in servicecar" v-bind:key="item">
        <td>{{ item.work_type }}</td>
        <td>{{ item.description }}</td>
        <td>{{ item.work_price }}</td>
      </tr>
    </tbody>
  </table>
  <div class="columns">
    <div class="column">
      <h3 class="is-size-3 has-text-left">Summa apmaksai kopā: Nav vel</h3>
    </div>
  </div>
  <div class="columns">
    <div class="column">
      <h3 class="is-size-3 has-text-left">Darbus veica: Nav vel</h3>
    </div>
  </div>
  <div class="field">
    <router-link class="button" :to="'/'">
      Sagatavot pavadzīmi PDF formātā
    </router-link>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "OrderCreatView",
  data() {
    return {
      customer: {},
      servicecar: [],
      partscar: [],
    };
  },
  mounted() {
    this.getOrderData();
    this.getServices();
    this.getParts();
  },
  methods: {
    convertDate() {
      let date = Date.now();
      let todaDay = new Date(date);
      return todaDay.toLocaleDateString("lv-LV");
    },
    async getOrderData() {
      await axios
        .get(`/customer/orderdata/${this.$route.params.id}`)
        .then((res) => {
          this.customer = res.data.info[0];
          console.log(this.customer);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getServices() {
      await axios
        .get(`/customer/services/${this.$route.params.id}`)
        .then((res) => {
          this.servicecar = res.data.servicecar;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getParts() {
      await axios
        .get(`/customer/parts/${this.$route.params.id}`)
        .then((res) => {
          this.partscar = res.data.partscar;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getPdfTest() {
      await axios
        .get(`/customer/hello_raims.pdf`)
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