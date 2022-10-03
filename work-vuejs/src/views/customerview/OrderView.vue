<template>
  <div>Order View</div>
  <div>{{ order.work_name }}</div>
  <div>{{ order.status }}</div>
  <div>{{ order.name }}</div>
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
    <h2>Klienta auto</h2>
    <button @click="reloadpage">R</button>
    <table class="table">
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
              >Auto</router-link
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
  name: "OrderView",
  data() {
    return {
      order: {},
      show: false,
      servicecar: [],
    };
  },
  mounted() {
    this.getOrder();
    this.getServices();
  },
  methods: {
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
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async createService() {
      let payload = {
        worktype: this.worktype,
        spendtime: this.spendtime,
        partname: this.partname,
        partcount: this.partcount,
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
  },
};
</script>