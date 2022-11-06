<template>
  <div class="card">
    <div class="card-content">
      <p class="subtitle">
        Klienta vārds: <strong>{{ customer.name }}</strong>
      </p>
      <p class="subtitle">
        Izveides datums: {{ convertDate(customer.create_date) }}
      </p>
      <p class="subtitle">Telefons: {{ customer.phone }}</p>
    </div>
  </div>
  <br />
  <div class="field">
    <button class="button" @click="showBlock(show)">
      Auto registrācijas forma
    </button>
  </div>
  <br />
  <form @submit.prevent="regcustcar" method="POST">
    <div class="block" v-bind:class="{ 'block-show': !show }">
      <div class="field">
        <label class="label">Modelis</label>
        <div class="control">
          <input
            class="input is-success"
            type="text"
            placeholder="Audi"
            v-model="carbrand"
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Auto numurs</label>
        <div class="control">
          <input
            class="input"
            type="text"
            placeholder="LV-XXXX"
            v-model="carnumber"
          />
        </div>
        <p class="help is-success" v-bind:class="{ 'block-show': numberexist }">
          Registrēts auto numurs
        </p>
      </div>
      <div class="field">
        <label class="label">VIN numurs</label>
        <div class="control">
          <input
            class="input"
            type="text"
            placeholder="VIN##########"
            v-model="vinnumber"
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Odometra rādītājs</label>
        <div class="control">
          <input
            class="input"
            type="numbers"
            placeholder="Nobraukums"
            v-model="odometer"
          />
        </div>
      </div>
      <div class="field">
        <button class="button">Registrēt auto</button>
      </div>
    </div>
  </form>
  <div class="columns is-justify-content-space-between is-flex">
    <div class="column">
      <h2 class="title">Klienta auto</h2>
    </div>
  </div>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>ID</th>
        <th>Modelis</th>
        <th>Auto Nr.</th>
        <th>VIN numurs</th>
        <th>Odometra rādītājs</th>
        <th>Izveides datums</th>
        <th>Darbības</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in cars" v-bind:key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.brand }}</td>
        <td>{{ item.number }}</td>
        <td>{{ item.vinnumber }}</td>
        <td>{{ item.odometer }}</td>
        <td>{{ item.create_date }}</td>
        <td>
          <router-link :to="'/' + item.customer_id + '/car/' + item.id"
            >Auto</router-link
          >
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import axios from "axios";

export default {
  name: "CustomerView",
  data() {
    return {
      cars: [],
      show: false,
      numberexist: true,
      customer: {},
      carbrand: "",
      carnumber: "",
      vinnumber: "",
      odometer: "",
    };
  },
  mounted() {
    this.getCustomer();
    this.getCars();
  },
  methods: {
    async getCustomer() {
      await axios
        .get(`/customer/${this.$route.params.id}`)
        .then((res) => {
          this.customer = res.data.customer[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getCars() {
      await axios
        .get(`/customer/cars/${this.$route.params.id}`)
        .then((res) => {
          this.cars = res.data.customerscars;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async regcustcar() {
      let payload = {
        carbrand: this.carbrand,
        carnumber: this.carnumber,
        vinnumber: this.vinnumber,
        odometer: this.odometer,
      };
      await axios
        .post(`/customer/carreg/${this.$route.params.id}`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          if (res.data.status === "exist_car") {
            this.numberexist = false;
          } else {
            this.reloadpage();
          }
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
<style>
.block-show {
  display: none;
}
</style>