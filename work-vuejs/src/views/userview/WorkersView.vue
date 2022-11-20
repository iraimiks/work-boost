<template>
<div>
    <h2 class="title">Darbinieki</h2>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Meklēt</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input class="input" v-model="searchWord" type="text" placeholder="Meklēt darbinieku" />
          </p>
        </div>
      </div>
    </div>
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
      <tbody v-if="searchWord != ''">
        <tr v-for="item in filterWorkers" v-bind:key="item">
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
      <tbody v-else>
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
      searchWord: ''
    };
  },
  computed: {
    filterWorkers() {
      return this.workers.filter(worker => {
        return worker.name.toLowerCase().indexOf(this.searchWord.toLowerCase()) != -1;
      });
    }
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