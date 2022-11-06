<template>
  <div class="card">
    <div class="card-content">
      <h2 class="title">Izveidot pasūtījumu un pievienot darbinieku</h2>
      <p class="subtitle">
        Auto: <strong>{{ car.brand }}</strong>
      </p>
      <p class="subtitle">
        Auto numurs: <strong>{{ car.number }}</strong>
      </p>
      <p class="subtitle">
        VIN: <strong>{{ car.vinnumber }}</strong>
      </p>
      <p class="subtitle">
        Odometrs: <strong>{{ car.odometer }}</strong>
      </p>
      <p class="subtitle">
        Izveides datums: <strong>{{ convertDate(car.create_date) }}</strong>
      </p>
    </div>
  </div>
  <br />
  <div class="field">
    <button class="button" @click="showBlock(show)">Pasūtījuma forma</button>
  </div>
  <form @submit.prevent="regorder" method="POST">
    <div class="block" v-bind:class="{ 'block-show': !show }">
      <div class="field">
        <label class="label">Izvēlies darbinieku</label>
        <div class="control">
          <div class="select">
            <select v-model="worker">
              <option v-for="item in workers" :value="item">
                {{ item.username }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <button class="button">Iveidot pasūtījumu</button>
      </div>
    </div>
  </form>
  <div class="columns is-justify-content-space-between is-flex">
    <div class="column">
      <h2 class="title">Auto pasūtījumi</h2>
    </div>
    <div class="column is-one-quarter">
      <button @click="reloadpage" class="button">Pārlādēt</button>
    </div>
  </div>

  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>ID</th>
        <th>Pasūtījums</th>
        <th>Status</th>
        <th>Darba veicējs</th>
        <th>Izveides datums</th>
        <th>Darbības</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in carorders" v-bind:key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.status }}</td>
        <td>{{ item.work_name }}</td>
        <td>{{ item.create_date }}</td>
        <td>
          <router-link :to="'/order/' + item.id">Darbs ar auto</router-link>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import axios from "axios";
export default {
  name: "CustomerCar",
  data() {
    return {
      car: {},
      workers: [],
      carorders: [],
      show: false,
      worker: "",
    };
  },
  mounted() {
    this.getWorkers();
    this.getCarOrders();
    this.getCar();
  },
  methods: {
    async getCar() {
      await axios
        .get(`/customer/car/${this.$route.params.id}`)
        .then((res) => {
          this.car = res.data.car[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getWorkers() {
      await axios
        .get(`/customer/workers`)
        .then((res) => {
          this.workers = res.data.workers;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async regorder() {
      let payload = {
        worker: this.worker.username,
        carid: this.$route.params.id,
        custid: this.$route.params.custid,
      };
      await axios
        .post(`/customer/order`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => console.log(error));
    },
    async getCarOrders() {
      await axios
        .get(`/customer/orders/${this.$route.params.id}`)
        .then((res) => {
          this.carorders = res.data.carorder;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    reloadpage() {
      window.location.reload();
    },
    showBlock(check) {
      this.show = !check;
    },
    convertDate(date) {
      this.date = new Date(date);
      return this.date.toLocaleDateString("lv-LV");
    },
  },
};
</script>
<style>
.block-show {
  display: none;
}
</style>