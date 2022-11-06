<template>
  <div class="card">
    <div class="card-content">
      <p class="subtitle">
        Darbu veic: <strong>{{ order.work_name }}</strong>
      </p>
      <p class="subtitle">
        Darba status:
        <span v-if="order.status === 'Darbs Sākts'" style="color: green">{{
          order.status
        }}</span>
        <span v-else="order.status === 'Darbs Beigts'" style="color: red">{{
          order.status
        }}</span>
      </p>
      <p class="subtitle">
        Pasūtījuma registrācijas kods: <strong>{{ order.name }}</strong>
      </p>
      <p class="subtitle">
        Darba uzsākšana: <strong>{{ convertDate(order.create_date) }}</strong>
      </p>
    </div>
  </div>
  <br />
  <div class="field">
    <button class="button" @click="showBlock(show)">
      Darba registrācija un detaļu registrācija
    </button>
  </div>
  <form @submit.prevent="createService" method="POST">
    <div class="block" v-bind:class="{ 'block-show': !show }">
      <div class="field">
        <label class="label">Darba veids</label>
        <div class="control">
          <div class="select">
            <select v-model="worktype">
              <option>Diagnostika</option>
              <option>Remonts</option>
              <option>Detaļas maiņa</option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <label class="label">Iztērētais laiks</label>
        <div class="control">
          <input
            class="input is-success"
            type="text"
            placeholder="Min"
            v-model="spendtime"
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Detaļas nosaukums</label>
        <div class="control">
          <input
            class="input is-success"
            type="text"
            placeholder="Riepas"
            v-model="partname"
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Detaļu skaits</label>
        <div class="control">
          <input
            class="input is-success"
            type="number"
            placeholder="Cipars"
            v-model="partcount"
          />
        </div>
      </div>
      <div class="field">
        <button class="button">Registrēt darbu</button>
      </div>
    </div>
  </form>
  <div>
    <div class="columns is-justify-content-space-between is-flex">
      <div class="column">
        <h2 class="title">Darbs ar auto</h2>
      </div>
      <div class="column is-one-quarter">
        <button @click="reloadpage" class="button">Pārlādēt</button>
      </div>
    </div>

    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Darba veids</th>
          <th>Iztērētais laiks</th>
          <th>Detaļas nosaukums</th>
          <th>Detaļu skaits</th>
          <th>Izveides datums</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in servicecar" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.work_type }}</td>
          <td>{{ item.spend_time }}</td>
          <td>{{ item.part_name }}</td>
          <td>{{ item.part_count }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/' + item.customer_id + '/car/' + item.id"
              >Labot</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
    <div class="field">
      <h2 class="title">Izviedot pavadzīmi</h2>
      <form @submit.prevent="createOrder" method="POST">
        <div class="field">
          <button class="button">Veidot</button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "OrderView",
  data() {
    return {
      order: {},
      show: false,
      servicecar: [],
      worktype: "",
      spendtime: "",
      partname: "",
      partcount: "",
    };
  },
  mounted() {
    this.getOrder();
    this.getServices();
  },
  methods: {
    async createOrder() {
      let payload = {
        cust_id: this.order.cust_id,
        order_id: this.$route.params.id,
      };
      await axios
        .post(`/customer/orderdata`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getOrder() {
      await axios
        .get(`/customer/order/${this.$route.params.id}`)
        .then((res) => {
          this.order = res.data.order[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getServices() {
      await axios
        .get(`/customer/services/${this.$route.params.id}`)
        .then((res) => {
          this.servicecar = res.data.servicecar;
          console.log(this.servicecar);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async createService() {
      let payload = {
        work_type: this.worktype,
        spend_time: this.spendtime,
        part_name: this.partname,
        part_count: this.partcount,
        order_id: this.orderid,
      };
      await axios
        .post(`/customer/service/${this.$route.params.id}`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showBlock(check) {
      this.show = !check;
    },
    reloadpage() {
      window.location.reload();
    },
    convertDate(date) {
      this.date = new Date(date);
      return this.date.toLocaleDateString("lv-LV");
    },
  },
};
</script>