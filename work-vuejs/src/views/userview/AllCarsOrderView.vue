<template>
  <h2 class="title">Visi darbi ar auto</h2>
  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <label class="label">Meklēt</label>
    </div>
    <div class="field-body">
      <div class="field">
        <p class="control">
          <input
            class="input"
            v-model="searchWord"
            type="text"
            placeholder="Meklēt auto reg. numuru"
          />
        </p>
      </div>
    </div>
  </div>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>ID</th>
        <th>Auto numurs</th>
        <th>Pasūtījums</th>
        <th>Darba status</th>
        <th>Darba veicējs</th>
        <th>Darbības</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in mergeData" v-bind:key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.number }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.status }}</td>
        <td>{{ item.work_name }}</td>
        <td>
          <div class="field has-addons">
            <p class="control">
              <router-link
                :to="'/dashboard/customers/' + item.customer_id"
                class="button"
                >Klients lapa</router-link
              >
            </p>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import axios from "axios";
export default {
  name: "AllCarsOrderView",
  data() {
    return {
      searchWord: "",
      orders: [],
      cars: [],
    };
  },
  computed: {
    mergeData() {
      const mergData = [];
      this.orders.forEach((order) => {
        const match = this.cars.find(
          (car) => parseInt(order.car_id) === car.id
        );
        if (match) {
          mergData.push({ ...order, ...match });
        }
      });
      return mergData;
    },
  },
  mounted() {
    this.getCarOrders();
    this.getCars();
  },
  methods: {
    async getCarOrders() {
      await axios
        .get("/customer/statuswork")
        .then((res) => {
          this.orders = res.data.orders;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async getCars() {
      await axios
        .get("/customer/cars")
        .then((res) => {
          this.cars = res.data.cars;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>