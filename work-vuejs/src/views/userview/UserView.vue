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
          <router-link class="button is-info" :to="'/dashboard/customers'">Apskatīt</router-link>
        </span>
      </p>
      <p class="card-footer-item">
        <span>
          <h3>Darbinieki: {{ workers.length }}</h3>
          <router-link class="button is-info" :to="'/dashboard/workers'">Apskatīt</router-link>
        </span>
      </p>
    </footer>
  </div>
  <hr />
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
          console.log(res);
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
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  }
};
</script>