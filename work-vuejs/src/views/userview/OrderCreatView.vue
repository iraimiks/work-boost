<template>
  <div class="card">
    <div class="card-content">
      <p class="subtitle">Pasūtījuma sagataves forma</p>
    </div>
  </div>
  <div class="columns">
    <div class="column is-half is-offset-one-quarter">
      <h3 class="is-size-3 has-text-centered">AUTOBOOST.LV</h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">Tel: 27015660</h3>
    </div>
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Pieņemšanas datums: {{ convertDate() }}
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">E-mail: autoboostlv@gmail.com</h3>
    </div>
    <div class="column is-6">
      <h3 class="is-size-4 has-text-left">
        Nodošanas datums: {{ convertDate() }}
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">Ipašnieks:</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">{{ customer.customer_name }}</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">Marka:</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">{{ customer.brand }}</h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">Tel:</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">{{ customer.phone }}</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">Reg. nr.:</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">{{ customer.number }}</h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">Addrese:</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">xxx</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">Nobraukums:</h3>
    </div>
    <div class="column is-3">
      <h3 class="is-size-4 has-text-left">{{ customer.odometer }}</h3>
    </div>
  </div>
  <h2>Detaļu saraksts</h2>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Nr.pk.</th>
        <th>Detaļas nosaukumms</th>
        <th>Gabals</th>
        <th>Cena</th>
      </tr>
    </thead>
    <tbody>
      <tr  v-for="item in services" v-bind:key="item">
        <td>1</td>
        <td>{{ item.part_name }}</td>
        <td>{{ item.part_count }}</td>
        <td>CENA NAV</td>
      </tr>
    </tbody>
  </table>
  <h2>Izdarītā darba saraksts</h2>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Nr.pk.</th>
        <th>Izpildītais darbs</th>
        <th>Cena</th>
      </tr>
    </thead>
    <tbody>
      <tr  v-for="item in services" v-bind:key="item">
        <td>1</td>
        <td>{{ item.work_type }}</td>
        <td>CENA</td>
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
import axios from 'axios'
export default {
  name: "OrderCreatView",
  data() {
    return {
      customer: {},
      services: [],
    };
  },
  mounted() {
    this.getOrderData()
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
          this.services = res.data.service_car;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
</script>