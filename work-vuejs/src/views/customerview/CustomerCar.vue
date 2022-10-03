<template>
  <div>Klienta Auto:</div>
  <div>{{ car.id }}</div>
  <div>{{ car.brand }}</div>
  <div>{{ car.number }}</div>
  <div>{{ car.vinnumber }}</div>
  <div>{{ car.odometer }}</div>
  <div>{{ car.create_date }}</div>
  <h3>Izveidot pasūtījumu un pievienot darbinieku</h3>
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
        <button class="button">Darbs auto</button>
      </div>
    </div>
  </form>

  <h2>Darbs auto</h2>
  <table class="table">
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
          <router-link :to="'/order/' + item.id"
            >Darbs ar auto</router-link
          >
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
  },
  methods: {
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