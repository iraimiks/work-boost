<template>
  <div class="card">
    <div class="card-content">
      <p class="title">Tavs Profils: {{ user }}</p>
      <p class="subtitle">Datums: {{ today }}</p>
    </div>
    <footer class="card-footer">
      <p class="card-footer-item">
        <span>
          <h3>Klienti: {{ customers.length }}</h3>
          <button @click="getItems(true)">Apskatīt</button>
        </span>
      </p>
      <p class="card-footer-item">
        <span>
          <h3>Darbinieki: {{ workers.length }}</h3>
          <button @click="getItems(false)">Apskatīt</button>
        </span>
      </p>
    </footer>
  </div>
  <hr />
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
      user: "",
      today: "",
    };
  },
  mounted() {
    this.getCustomers(),
      this.getWorkers(),
      this.getItems(this.what),
      (this.user = this.$store.state.user.data[0].username),
      (this.date = new Date()),
      (this.today = this.date.toLocaleDateString("lv-LV"));
  },
  methods: {
    async getCustomers() {
      await axios
        .get("/customer/list")
        .then((res) => {
          this.customers = res.data.customers;
          this.items = this.customers;
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