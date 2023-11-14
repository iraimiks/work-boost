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
  <hr>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Auto servisa addrese:
        <div class="select">
          <select v-model="streetService">
            <option>Liepājas iela 5 Ludza</option>
            <option>Varoņu iela 39 Rēzekne</option>
          </select>
        </div>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Klienta Banka: <strong>{{ customer.customer_bank_name }}</strong>
      </h3>
    </div>
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        <strong>{{ customer.customer_bank_acc }}</strong>
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
        Reg. nr. vai Personas Kods: <strong>{{ customer.customer_number }}</strong>
      </h3>
    </div>
  </div>
  <div class="columns">
    <div class="column is-6 border-box">
      <h3 class="is-size-4 has-text-left">
        Addrese: <strong>{{ customer.customer_street }}</strong>
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
            <option>Skaidra nauda</option>
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
      payOption: "",
      streetService: "",
      priceInWords: "",
    };
  },
  mounted() {
    this.getOrderData();
    this.getServices();
    this.getParts();
  },
  computed: {
    
  },
  methods: {
    getFullPartPrice(tax) {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return tax === true ? formatter.format(
        this.partscar.reduce((p, all) => p + parseFloat(all.full_price), 0) +
          this.partscar.reduce((p, all) => p + parseFloat(all.full_price), 0) *
            0.21
      ) : formatter.format(
        this.partscar.reduce((p, all) => p + parseFloat(all.full_price), 0)
      );
    },
    getFullServicePrice(tax) {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return tax === true ? formatter.format(
        this.servicecar.reduce((p, all) => p + parseFloat(all.work_price), 0) +
          this.servicecar.reduce((p, all) => p + parseFloat(all.work_price), 0) *
            0.21
      ) : formatter.format(
        this.servicecar.reduce((p, all) => p + parseFloat(all.work_price), 0)
      );
    },
    getFullPrice(tax) {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(
        parseFloat(parseFloat(this.getFullServicePrice(tax))) + parseFloat(this.getFullPartPrice(tax))
      );
    },
    getFullCount() {
      let spend_count = this.servicecar.reduce((p, all) => p + parseInt(all.spend_time), 0);
      let part_count = this.partscar.reduce((p, all) => p + parseInt(all.part_count), 0);
      return parseInt(spend_count) + parseInt(part_count);
    },
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
      let full_no_tax = this.getFullPrice(false);
      let full_tax = this.getFullPrice(true);
      let tax = full_tax - full_no_tax;
      let payload = {
        full_service_price: this.getFullServicePrice(false),
        full_part_price: this.getFullPartPrice(false),
        full_count: this.getFullCount(),
        full_tax: tax,
        pay_option: this.payOption,
        street_service: this.streetService,
        full_price_no_tax: full_no_tax,
        full_price: full_tax,
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