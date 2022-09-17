<template>
  <div>
    <h2>Registrētie klienti</h2>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Vārds</th>
          <th>Talrunis</th>
          <th>Izveides datums</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in customers" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.customer_name }}</td>
          <td>{{ item.phone }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link to="/dashboard/"
              >Registrēt klientu</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "CustomersView",

  data() {
    return {
      customers: [],
    };
  },
  mounted() {
    this.getCustomers();
  },
  methods: {
    async getCustomers() {
      await axios
        .get("/customer/list")
        .then((res) => {
          this.customers = res.data.customers;
          console.log(this.customers);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>