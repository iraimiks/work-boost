<template>
  <div>Klients:</div>
  <div>{{ customer.id }}</div>
  <div>{{ customer.customer_name }}</div>
  <div>{{ customer.create_date }}</div>

  <br />
  <div class="field">
    <button class="button" @click="showBlock(show)">
      Auto registrācijas forma
    </button>
  </div>
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
        <p class="help is-success">Registrēts auto numurs</p>
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
        <p class="help is-success">Registrēts auto vin</p>
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
  <div>
    <h2>Klienta auto</h2>
    <button @click="reloadpage">R</button>
    <table class="table">
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
            <router-link :to="'/'+ item.customer_id + '/car/' + item.id"
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
  name: "CustomerView",
  data() {
    return {
      cars: [],
      show: false,
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
          console.log(this.cars)
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
    }
  },
};
</script>
<style>
.block-show {
  display: none;
}
</style>