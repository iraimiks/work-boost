<template>
  <div class="card">
    <div class="card-content">
      <p class="title">Pasūtījuma sagataves forma</p>
    </div>
    <footer class="card-footer">
      <router-link
        :to="'/order/' + this.customer.order_id"
        class="card-footer-item"
        >Darbs ar auto lapa</router-link
      >
    </footer>
  </div>
  <hr />
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Nodošanas datums: <strong>{{ convertDate(Date.now()) }}</strong>
      </h3>
    </div>
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Rēķina Nr. <strong>{{ customer.order_name }}</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Pieņemšanas datums:
        <strong>{{ convertDate(customer.create_in) }}</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Preču nosūtītājs: <strong>AUTOBOOST SIA</strong>
      </h3>
    </div>
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        <strong>LV40203418867</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Adrese: <strong>Liepājas iela 5 Ludza</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Norēķinu rekvizīti: <strong>Citadele banka</strong>
      </h3>
    </div>
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        <strong>LV47PARXO027844410001</strong>
      </h3>
    </div>
  </div>
  <hr />
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Pakalpojuma saņēmējs: <strong>{{ customer.customer_name }}</strong>
      </h3>
    </div>
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Reg. nr.: <strong><input v-model="customerRegNumber" /></strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Addrese: <strong><input v-model="customerAddress" /></strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-8 border-box">
      <h3 class="is-size-4 has-text-left">
        Pakalpojuma saņemšanas vieta: <strong>Liepājas iela 5 Ludza</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-8 border-box">
      <h3 class="is-size-4 has-text-left">
        Apmaksas veids un kārtība:
        <div class="select">
          <select v-model="payOption">
            <option>Pārskaitījums</option>
            <option>Ar karti</option>
          </select>
        </div>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Auto: <strong>{{ customer.brand }} {{ customer.number }}</strong>
      </h3>
    </div>
  </div>
  <h4  class="is-size-4">Detaļu saraksts</h4>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>ID</th>
        <th>Detaļas nosaukums</th>
        <th>Detaļas skaits</th>
        <th>Vienas vienības cena</th>
        <th>Pilnā cena</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in partscar" v-bind:key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.part_name }}</td>
        <td>{{ item.part_count }}</td>
        <td>{{ item.part_price }}</td>
        <td>{{ item.full_price }}</td>
      </tr>
    </tbody>
  </table>
  <div class="columns">
    <div class="column">
      <h4 class="is-size-4 has-text-left">
        Par detaļām kopā: <strong>{{ getFullPartPrice }}</strong> euro. Summa ir
        ar 21% nodokli.
      </h4>
    </div>
  </div>
  <h4 class="is-size-4" >Izdarītā darba saraksts</h4>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Darba veids</th>
        <th>Darba apraksts</th>
        <th>Cena</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in servicecar" v-bind:key="item">
        <td>{{ item.work_type }}</td>
        <td>{{ item.description }}</td>
        <td>{{ item.work_price }}</td>
      </tr>
    </tbody>
  </table>
  <div class="columns">
    <div class="column">
      <h4 class="is-size-4 has-text-left">
        Par darbu kopā: <strong>{{ getFullServicePrice }}</strong> euro. Summa
        ir ar 21% nodokli.
      </h4>
    </div>
  </div>
  <hr />
  <div class="columns">
    <div class="column">
      <h4 class="is-size-4 has-text-left">Kopā: <strong>{{ getFullPrice }}</strong> euro</h4>
    </div>
    <div class="column">
      <h4 class="is-size-4 has-text-left">
        Vārdiem: <input v-model="priceInWords" />
      </h4>
    </div>
  </div>
  <div class="columns">
    <div class="column">
      <h4 class="is-size-4 has-text-left">
        Iznsniedza: <input v-model="orderPrepName" />
      </h4>
    </div>
    <div class="column">
      <h4 class="is-size-4 has-text-left">
        Saņēma: <input v-model="orderGetName" />
      </h4>
    </div>
  </div>
  <hr />
  <div class="columns">
    <div class="column">
      <h2 class="is-size-2 has-text-left">Darbs noslēgšana</h2>
    </div>
  </div>
  <div class="columns">
    <div class="column">
      <button class="button is-warning is-light" @click="getPdfTest">
        Sagatavot pdf
      </button>
    </div>
    <div class="column">
      <button class="button is-danger is-light" @click="finishWork">
        Darbs Pabeigts
      </button>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "OrderCreatView",
  data() {
    return {
      customer: {},
      servicecar: [],
      partscar: [],
      customerRegNumber: "",
      customerAddress: "",
      payOption: "",
      orderPrepName: "",
      orderGetName: "",
      priceInWords: "",
    };
  },
  mounted() {
    this.getOrderData();
    this.getServices();
    this.getParts();
  },
  computed: {
    getFullPartPrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(
        this.partscar.reduce((p, all) => p + parseInt(all.full_price), 0) +
          this.partscar.reduce((p, all) => p + parseInt(all.full_price), 0) *
            0.21
      );
    },
    getFullServicePrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(
        this.servicecar.reduce((p, all) => p + parseInt(all.work_price), 0) +
          this.servicecar.reduce((p, all) => p + parseInt(all.work_price), 0) *
            0.21
      );
    },
    getFullPrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(
        parseFloat(this.getFullServicePrice) + parseFloat(this.getFullPartPrice)
      );
    },
  },
  methods: {
    convertDate(date) {
      this.date = new Date(date);
      return this.date.toLocaleDateString("lv-LV");
    },
    async getOrderData() {
      await axios
        .get(`/customer/orderdata/${this.$route.params.id}`)
        .then((res) => {
          this.customer = res.data.info[0];
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
    async getParts() {
      await axios
        .get(`/customer/parts/${this.$route.params.id}`)
        .then((res) => {
          this.partscar = res.data.partscar;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getPdfTest() {
      let payload = {
        full_service_price: this.getFullServicePrice,
        full_part_price: this.getFullPartPrice,
        customer_reg_number: this.customerRegNumber,
        customer_address: this.customerAddress,
        pay_option: this.payOption,
        full_price: this.getFullPrice,
        order_prep_name: this.orderPrepName,
        order_get_name: this.orderGetName,
        price_in_words: this.priceInWords,
        order_id: this.$route.params.id,
      };

      await axios
        .post(`/customer/addorderdata`, payload, {
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
      await axios
        .get(`/customer/pdforder/${this.$route.params.id}`, {
          responseType: "blob",
        })
        .then((res) => {
          console.log(res);
          const blob = new Blob([res.data], {
            type: res.headers["content-type"],
          });
          const objectUrl = URL.createObjectURL(blob);
          this.pdfsrc = objectUrl;
          window.open(this.pdfsrc, "_blank");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async finishWork() {
      let payload = {
        order_status: "Darbs Beigts",
      };
      await axios
        .post(`/customer/finishwork/${this.$route.params.id}`, payload, {
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
  },
};
</script>
<style>
.border-box {
  border: black solid 1px;
}
</style>