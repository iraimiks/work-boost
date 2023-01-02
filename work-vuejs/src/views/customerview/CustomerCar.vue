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
    <footer class="card-footer">
      <a @click="showEditBlock(showEdit)" class="card-footer-item">Labot</a>
      <router-link
        :to="'/dashboard/customers/' + this.$route.params.custid"
        class="card-footer-item ">Klienta lapa</router-link
      >
    </footer>
  </div>
  <div class="card" v-bind:class="{ 'block-show': !showEdit }">
    <div class="card-content">
      <div class="content">
        <form @submit.prevent="editCustomerCar" method="POST">
          <div class="block">
            <div class="field">
              <label class="label">Modelis</label>
              <div class="control">
                <input
                  class="input is-success"
                  type="text"
                  placeholder="Auto modelis un tā nosaukums"
                  v-model="car.brand"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Auto numurs</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="LV-XXXX"
                  v-model="car.number"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">VIN numurs</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="VIN##########"
                  v-model="car.vinnumber"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Odometra rādītājs</label>
              <div class="control">
                <input
                  class="input"
                  type="numbers"
                  placeholder="Nobraukums"
                  v-model="car.odometer"
                />
              </div>
            </div>
            <div class="field">
              <button class="button is-warning">Labot auto</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
  <br />
  <div class="columns is-justify-content-space-between is-flex">
    <div class="column">
      <h2 class="title">Auto pasūtījumi</h2>
    </div>
  </div>
  <hr />
  <div class="field">
    <button class="button is-info" @click="showBlock(show)">
      Pasūtījuma forma
    </button>
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
        <button class="button is-warning">Izveidot pasūtījumu</button>
      </div>
    </div>
  </form>

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
        <td><span v-if="item.status === 'Darbs Sākts'" style="color: green">{{
          item.status
        }}</span>
        <span v-else="item.status === 'Darbs Beigts'" style="color: red">{{
          item.status
        }}</span></td>
        <td>{{ item.work_name }}</td>
        <td>{{ item.create_date }}</td>
        <td>
          <router-link class="button" :to="'/order/' + item.id">Darbs ar auto</router-link>
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
      showEdit: false,
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
    async editCustomerCar() {
      let payload = {
        car_brand: this.car.brand,
        car_number: this.car.number,
        vinnumber: this.car.vinnumber,
        odometer: this.car.odometer,
      };
      await axios
        .post(`/customer/caredit/${this.$route.params.id}`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          this.reloadpage();
          console.log(res);
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
          this.reloadpage();
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
    showEditBlock(check) {
      this.showEdit = !check;
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