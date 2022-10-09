<template>
  <div>Tavs Profils: </div>
  <div>Datums: </div>
  <div>
    <h2>Darba aktivitātes</h2>
    <div class="columns">
      <div class="column">
        <h3>Klienti</h3>
        <div>{{ customers.length }}</div>
        <button @click="getItems(true)">Apskatīt</button>
      </div>
      <div class="column">
        <h3>Darbinieki</h3>
        <div>{{ workers.length }}</div>
        <button @click="getItems(false)">Apskatīt</button>
      </div>
    </div>
  </div>
  <div>
    <h2>Darbi</h2>
    <UserViewTable :items="items" />
  </div>
</template>
<script>
import UserViewTable from "../../components/UserViewTable.vue";
import axios from "axios";
export default {
  name: "UserView",
  components: {
    UserViewTable,
  },
  data() {
    return {
      customers: [],
      workers: [],
      items: [],
      what: true,
    };
  },
  mounted() {
    this.getCustomers(), this.getWorkers(), this.getItems(this.what);
  },
  methods: {
    async getCustomers() {
      await axios
        .get("/customer/list")
        .then((res) => {
          this.customers = res.data.customers;
          console.log(this.customers)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getWorkers() {
      await axios
        .get("/customer/workers")
        .then((res) => {
          this.workers = res.data.workers;
          console.log(this.workers)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getItems(what) {
      if (what) {
        this.items = this.customers;
      } else {
        this.items = this.workers;
      }
    },
  },
};
</script>