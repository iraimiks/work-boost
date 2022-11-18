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
  <div class="columns">
    <div class="column">
      <div class="field">
        <button class="button" @click="showBlock(show)">
          Darba registrācija
        </button>
      </div>
    </div>
    <div class="column">
      <form>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Stundas likme</label>
          </div>
          <div class="field-body">
            <div class="field has-addons">
              <p class="control">
                <span class="select">
                  <select>
                    <option>10</option>
                    <option>15</option>
                    <option>20</option>
                  </select>
                </span>
              </p>
              <p class="control">
                <input class="input" type="text" placeholder="0.00" />
              </p>
              <p class="control">
                <a class="button"> Noteikt </a>
              </p>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Grūtības pakāpe</label>
          </div>
          <div class="field-body">
            <div class="field has-addons">
              <p class="control">
                <span class="select">
                  <select>
                    <option>1 %</option>
                    <option>2 %</option>
                    <option>3 %</option>
                  </select>
                </span>
              </p>
              <p class="control">
                <input class="input" type="text" placeholder="0" />
              </p>
              <p class="control">
                <a class="button"> Noteikt </a>
              </p>
            </div>
          </div>
        </div>
      </form>
    </div>
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
        <label class="label">Apraksts</label>
        <div class="control">
          <input class="input is-success" type="text" v-model="description" />
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
        <label class="label">Darba cena</label>
        <div class="control">
          <input
            class="input is-success"
            type="text"
            placeholder="0.00"
            v-model="workprice"
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
    </div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Darba veids</th>
          <th>Iztērētais laiks</th>
          <th>Darba laiks</th>
          <th>Darba samaksa</th>
          <th>Izveides datums</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in servicecar" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.work_type }}</td>
          <td>{{ item.description }}</td>
          <td>{{ item.spend_time }}</td>
          <td>{{ item.work_price }}</td>
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
      <button class="button" @click="showPartBlock(partForm)">
        Detaļu registrācija
      </button>
    </div>
    <form @submit.prevent="creatPart" method="POST">
      <div class="block" v-bind:class="{ 'block-show': !partForm }">
        <div class="field">
          <label class="label">Detaļas nosaukums</label>
          <div class="control">
            <input class="input is-success" type="text" v-model="partname" />
          </div>
        </div>
        <div class="field">
          <label class="label">Daudzums</label>
          <div class="control">
            <input
              class="input is-success"
              type="text"
              placeholder="0"
              v-model="partcount"
            />
          </div>
        </div>
        <div class="field">
          <label class="label">Detaļas cena</label>
          <div class="control">
            <input
              class="input is-success"
              type="text"
              placeholder="0.00"
              v-model="partprice"
            />
          </div>
        </div>
        <div class="field">
          <label class="label">Kopā</label>
          <div class="control">
            <input
              class="input is-success"
              type="text"
              placeholder="0.00"
              v-model="fullprice"
            />
          </div>
        </div>
        <div class="field">
          <button class="button">Registrēt detaļu</button>
        </div>
      </div>
    </form>
    <div class="columns is-justify-content-space-between is-flex">
      <div class="column">
        <h2 class="title">Auto detaļas</h2>
      </div>
    </div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Detaļas nosaukums</th>
          <th>Detaļas skaits</th>
          <th>Vienas vienības cena</th>
          <th>Pilnā cena</th>
          <th>Izveides datums</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in partscar" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.part_name }}</td>
          <td>{{ item.part_count }}</td>
          <td>{{ item.part_price }}</td>
          <td>{{ item.full_price }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/' + item.id">Labot</router-link>
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
      partForm: false,
      servicecar: [],
      partscar: [],
      worktype: "",
      workprice: "",
      spendtime: "",
      partname: "",
      partcount: "",
      partprice: "",
      fullprice: "",
      description: "",
    };
  },
  mounted() {
    this.getOrder();
    this.getServices();
    this.getParts();
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
          window.location.href = "/creadorder/" + this.$route.params.id;
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
    async creatPart() {
      let payload = {
        part_name: this.partname,
        description: this.description,
        part_count: this.partcount,
        part_price: this.partprice,
        full_price: this.fullprice,
      };
      await axios
        .post(`/customer/part/${this.$route.params.id}`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          console.log(res);
          this.reloadpage();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async createService() {
      let payload = {
        work_type: this.worktype,
        description: this.description,
        spend_time: this.spendtime,
        work_price: this.workprice,
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
          this.reloadpage();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showBlock(check) {
      this.show = !check;
    },
    showPartBlock(check) {
      this.partForm = !check;
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