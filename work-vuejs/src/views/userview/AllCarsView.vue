<template>
  <div>
    <h2 class="title">Auto</h2>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Auto marka</th>
          <th>Auto numurs</th>
          <th>Odometrs</th>
          <th>VIN</th>
          <th>Izveides datums</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in cars" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.brand }}</td>
          <td>{{ item.number }}</td>
          <td>{{ item.odometer }}</td>
          <td>{{ item.vinnumber }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <div class="field has-addons">
                <p class="control">
                <router-link :to="'/dashboard/customers/' + item.customer_id"
               class="button">Klients lapa</router-link
            >
            <router-link :to="'/dashboard/customers/' + item.id"
              class="button">Darbinieka lapa</router-link
            >
                </p>
            </div>
            
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: "AllCarsView",
  data() {
    return {
      cars: [],
    };
  },
  mounted() {
    this.getAllCars();
  },
  methods: {
    async getAllCars() {
      await axios
        .get("/customer/cars")
        .then((res) => {
          this.cars = res.data.cars;
          console.log(this.cars);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>