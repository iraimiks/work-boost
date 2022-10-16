<template>
<div>
    <h2 class="title">Darbinieki</h2>
    <table class="table is-fullwidth">
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
        <tr v-for="item in workers" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.phone }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/dashboard/customers/' + item.id "
              >Darbinieka lapa</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: "WorkersView",
  data() {
    return {
      workers: [],
    };
  },
  mounted() {
    this.getWorkers();
  },
  methods: {
    async getWorkers() {
      await axios
        .get("/customer/workers")
        .then((res) => {
          this.workers = res.data.workers;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>