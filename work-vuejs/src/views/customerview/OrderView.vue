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
  <div class="columns is-justify-content-space-between is-flex">
    <div class="column">
      <h2 class="title">Darbs ar auto</h2>
    </div>
  </div>
  <div class="columns">
    <div class="column">
      <div class="field">
        <button class="button is-info" @click="showBlock(show)">
          Darba registrācija
        </button>
      </div>
    </div>
  </div>
  <form
    class="box block"
    @submit.prevent="createService"
    method="POST"
    v-bind:class="{ 'block-show': !show }"
  >
    <div class="field">
      <label class="label">Darba veids</label>
      <div class="control">
        <div class="select">
          <select v-model="worktype">
            <option>Diagnostika</option>
            <option>Remonts</option>
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
          placeholder="Darbas"
          v-model="spendtime"
        />
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Stundas likme euro</label>
      </div>
      <div class="field-body">
        <div class="field has-addons">
          <p class="control">
            <input
              class="input"
              type="number"
              min="0"
              max="100"
              v-model="hourRate"
              placeholder="0"
            />
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Grūtības pakāpe %</label>
      </div>
      <div class="field-body">
        <div class="field has-addons">
          <p class="control">
            <input
              class="input"
              type="number"
              min="0"
              max="100"
              v-model="rateValue"
              placeholder="0"
            />
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Darba cena</label>
      </div>
      <div class="field-body">
        <div class="field has-addons">
          <p class="control">
            {{ getWorkPrice }}
          </p>
        </div>
      </div>
    </div>
    <div class="field">
      <button class="button is-warning is-light">Registrēt darbu</button>
    </div>
  </form>

  <form
    @submit.prevent="editRowData"
    method="POST"
    class="box"
    v-bind:class="{ 'block-show': !showEdit }"
  >
    <div class="field">
      <label class="label">ID:</label>
      <div class="control">
        <p>{{ serviceEditObj.id }}</p>
      </div>
    </div>
    <div class="field">
      <label class="label">Darba veids</label>
      <div class="control">
        <div class="select">
          <select v-model="serviceEditObj.work_type">
            <option>Diagnostika</option>
            <option>Remonts</option>
          </select>
        </div>
      </div>
    </div>
    <div class="field">
      <label class="label">Apraksts</label>
      <div class="control">
        <input
          class="input is-success"
          type="text"
          v-model="serviceEditObj.description"
        />
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Darba laiks:</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input class="input" v-model="serviceEditObj.spend_time" />
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Stundas likme euro:</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input
              class="input"
              type="number"
              min="0"
              max="100"
              v-model="hourRateEdit"
              placeholder="0"
            />
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Grūtības pakāpe %:</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input
              class="input"
              type="number"
              min="0"
              max="100"
              v-model="rateValueEdit"
              placeholder="0"
            />
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Darba cena:</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            {{ getFullServiceEditPrice }} euro
          </p>
        </div>
      </div>
    </div>
    <div class="field">
      <button class="button is-warning">Apstiprināt</button>
    </div>
  </form>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>ID</th>
        <th>Darba veids</th>
        <th>Apraksts</th>
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
          <a @click="showEditBlock(showEdit, item.id)" class="button is-warning">Labot</a>
        </td>
      </tr>
    </tbody>
  </table>
  <hr />
  <div class="columns is-justify-content-space-between is-flex">
    <div class="column">
      <h2 class="title">Auto detaļas</h2>
    </div>
  </div>
  <div class="field">
    <button class="button is-info" @click="showPartBlock(partForm)">
      Detaļu registrācija
    </button>
  </div>
  <form
    @submit.prevent="creatPart"
    method="POST"
    class="box block"
    v-bind:class="{ 'block-show': !partForm }"
  >
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
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Cena kopā:</label>
      </div>
      <div class="field-body">
        <div class="field has-addons">
          <p class="control">{{ getFullPartPrice }} euro</p>
        </div>
      </div>
    </div>
    <div class="field">
      <button class="button is-warning is-light">Registrēt detaļu</button>
    </div>
  </form>
  <form
    @submit.prevent="editPartRowData"
    method="POST"
    class="box"
    v-bind:class="{ 'block-show': !showPartEdit }"
  >
    <div class="field">
      <label class="label">ID:</label>
      <div class="control">
        <p>{{ partEditObj.id }}</p>
      </div>
    </div>
    <div class="field">
      <label class="label">Detaļas nosaukums</label>
      <div class="control">
        <input
          class="input is-success"
          type="text"
          v-model="partEditObj.part_name"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Daudzums</label>
      <div class="control">
        <input
          class="input is-success"
          type="text"
          placeholder="0"
          v-model="partEditObj.part_count"
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
          v-model="partEditObj.part_price"
        />
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Cena kopā:</label>
      </div>
      <div class="field-body">
        <div class="field has-addons">
          <p class="control">{{ this.getFullPartEditPrice }} euro</p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Izveides datums</label>
      </div>
      <div class="field-body">
        <div class="field has-addons">
          <p class="control">{{ partEditObj.create_date }}</p>
        </div>
      </div>
    </div>
    <div class="field">
      <button class="button is-warning">Apstiprināt</button>
    </div>
  </form>
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
          <a @click="showEditPartBlock(showPartEdit, item.id)"  class="button is-warning">Labot</a>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="field">
    <h2 class="title">Izviedot pavadzīmi</h2>
    <form @submit.prevent="createOrder" method="POST">
      <div class="field">
        <button class="button is-warning is-light">Veidot</button>
      </div>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "OrderView",
  data() {
    return {
      order: {},
      serviceEditObj: {},
      partEditObj: {},
      show: false,
      partForm: false,
      servicecar: [],
      partscar: [],
      worktype: "",
      spendtime: 0,
      partname: "",
      partcount: 0,
      partprice: 0,
      description: "",
      hourRate: 0,
      rateValue: 0,
      showEdit: false,
      showPartEdit: false,
      hourRateEdit: 0,
      rateValueEdit: 0,
    };
  },
  computed: {
    getWorkPrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      });
      return formatter.format(
        this.spendtime * this.hourRate + (this.hourRate * this.rateValue) / 100
      );
    },
    getFullPartPrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(this.partcount * this.partprice);
    },
    getFullServiceEditPrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(
        this.serviceEditObj.spend_time * this.hourRateEdit +
          (this.hourRateEdit * this.rateValueEdit) / 100
      );
    },
    getFullPartEditPrice() {
      const formatter = new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        style: "decimal",
        useGrouping: false,
      });
      return formatter.format(
        this.partEditObj.part_count * this.partEditObj.part_price
      );
    },
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
        part_count: this.partcount,
        part_price: this.partprice,
        full_price: this.getFullPartPrice,
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
        work_price: this.getWorkPrice,
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
    async editRowData() {
      let payload = {
        work_type: this.serviceEditObj.work_type,
        description: this.serviceEditObj.description,
        spend_time: this.serviceEditObj.spend_time,
        work_price: this.getFullServiceEditPrice,
      };
      await axios
        .post(`/customer/serviceedit/${this.serviceEditObj.id}`, payload, {
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
    async editPartRowData() {
      let payload = {
        part_name: this.partEditObj.part_name,
        part_count: this.partEditObj.part_count,
        part_price: this.partEditObj.part_price,
        full_price: this.getFullPartEditPrice,
      };
      await axios
        .post(`/customer/partedit/${this.partEditObj.id}`, payload, {
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
    showEditBlock(check, id) {
      this.showEdit = !check;
      this.serviceEditObj = this.servicecar.find((obj) => obj.id === id);
    },
    showEditPartBlock(check, id) {
      this.showPartEdit = !check;
      this.partEditObj = this.partscar.find((obj) => obj.id === id);
      console.log(this.partEditObj);
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