<template>
  <div class="card">
    <div class="card-content">
      <p class="subtitle">
        Klienta vārds: <strong>{{ customer.name }}</strong>
      </p>
      <p class="subtitle">
        Izveides datums:
        <strong>{{ convertDate(customer.create_date) }}</strong>
      </p>
      <p class="subtitle">
        Telefons: <strong>{{ customer.phone }}</strong>
      </p>
      <hr />
      <p class="subtitle">
        Klienta tips: <strong>{{ customer_data.customer_type }}</strong>
      </p>
      <p class="subtitle">
        Klienta reg. nr. vai personas kods:
        <strong>{{ customer_data.customer_number }}</strong>
      </p>
      <p class="subtitle">
        Addrese: <strong>{{ customer_data.customer_street }}</strong>
      </p>
      <p class="subtitle">
        Banka:
        <strong>{{ customer_data.customer_bank_name }}</strong>
      </p>
      <p class="subtitle">
        Bankas konts:
        <strong>{{ customer_data.customer_bank_acc }}</strong>
      </p>
    </div>
    <footer class="card-footer">
      <a @click="showEditBlock(showEdit)" class="card-footer-item">Labot</a>
      <a @click="showDataFormBlock(showDataForm)" class="card-footer-item"
        >Pievienot datus klienta</a
      >
      <form @submit.prevent="deleteCustomer" method="POST">
        <button class="card-footer-item button is-danger">Dzēst klientu</button>
      </form>
    </footer>
  </div>
  <div class="card" v-bind:class="{ 'block-show': !showEdit }">
    <div class="card-content">
      <div class="content">
        <form @submit.prevent="editCustomerData" method="POST">
          <div class="field">
            <label class="label">Klienta vārds</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                placeholder="Vārds Uzvārds vai uzņēmuma nosaukums"
                v-model="customer.name"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Telefons</label>
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="2*******"
                v-model="customer.phone"
              />
            </div>
          </div>
          <hr />
          <div class="field">
            <label class="label">Klienta veids</label>
            <div class="control">
              <div class="select">
                <select v-model="customer_data.customer_type">
                  <option>Fizisks</option>
                  <option>Juridisks</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="label">Reg. nr. vai Personas kods</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_data.customer_number"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Adrese</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_data.customer_street"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Norēķinu banka</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_data.customer_bank_name"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Norēķinu konts</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_data.customer_bank_acc"
              />
            </div>
          </div>
          <div class="field">
            <button class="button is-warning">Labot datus</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <div class="card" v-bind:class="{ 'block-show': !showDataForm }">
    <div class="card-content">
      <div class="content">
        <form @submit.prevent="regCustomerData" method="POST">
          <div class="field">
            <label class="label">Klienta veids</label>
            <div class="control">
              <div class="select">
                <select v-model="customer_type">
                  <option>Fizisks</option>
                  <option>Juridisks</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="label">Reg. nr. vai Personas kods</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_number"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Adrese</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_street"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Norēķinu banka</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_bank_name"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Norēķinu konts</label>
            <div class="control">
              <input
                class="input is-success"
                type="text"
                v-model="customer_bank_acc"
              />
            </div>
          </div>
          <div class="field">
            <button class="button is-warning">Pievienot datus</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <hr />
  <div class="field">
    <button class="button is-info" @click="showBlock(show)">
      Auto registrācijas forma
    </button>
  </div>
  <hr />
  <br />
  <form @submit.prevent="regCustomerCar" method="POST">
    <div class="block" v-bind:class="{ 'block-show': !show }">
      <div class="field">
        <label class="label">Modelis</label>
        <div class="control">
          <input
            class="input is-success"
            type="text"
            placeholder="Auto modelis un tā nosaukums"
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
        <button class="button is-warning">Registrēt auto</button>
      </div>
    </div>
  </form>
  <br />
  <div class="columns is-justify-content-space-between is-flex">
    <div class="column">
      <h2 class="title">Klienta auto</h2>
    </div>
    <div class="column" v-bind:class="{ 'block-show': !showWarrning }">
      <div class="notification is-danger">Eksistē pasūtījums</div>
    </div>
    <div class="column" v-bind:class="{ 'block-show': !showCarWarrning }">
      <div class="notification is-danger">Eksistē auto</div>
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
        <td v-if="item.number === ''">- - -</td>
        <td v-else>{{ item.number }}</td>
        <td v-if="item.vinnumber === ''">- - -</td>
        <td v-else>{{ item.vinnumber }}</td>
        <td v-if="item.odometer === ''">- - -</td>
        <td v-else>{{ item.odometer }}</td>
        <td>{{ convertDate(item.create_date) }}</td>
        <td>
          <div class="columns">
            <div class="column">
              <router-link
                class="button"
                :to="'/' + item.customer_id + '/car/' + item.id"
                >Izveidot pasūtījumu</router-link
              >
            </div>
            <div class="column">
              <form @submit.prevent="delCustomerCar(item)" method="POST">
                <div class="field">
                  <button class="button is-danger">Dzēst Auto</button>
                </div>
              </form>
            </div>
          </div>
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
      showEdit: false,
      showDataForm: false,
      showWarrning: false,
      showCarWarrning: false,
      customer: {},
      customer_data: {},
      carbrand: "",
      carnumber: "",
      vinnumber: "",
      odometer: "",
      customer_type: "",
      customer_number: "",
      customer_street: "",
      customer_bank_name: "",
      customer_bank_acc: "",
    };
  },
  mounted() {
    this.getCustomer();
    this.getCars();
    this.getCustomerType();
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
    async getCustomerType() {
      await axios
        .get(`/customer/customerdata/${this.$route.params.id}`)
        .then((res) => {
          this.customer_data = res.data.customer_data[0];
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
    async deleteCustomer() {
      let payload = {
        customer_id: this.customer.id,
      };
      await axios
        .post(`/customer/customerdel`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          if (res.data.status === "customer_delete") {
            window.location.href = "/dashboard/customers";
          } else {
            this.showCarWarrningBlock(false);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async editCustomerData() {
      let payload = {
        edit_name: this.customer.name,
        edit_phone: this.customer.phone,
        edit_customer_type: this.customer_data.customer_type,
        edit_customer_number: this.customer_data.customer_number,
        edit_customer_street: this.customer_data.customer_street,
        edit_customer_name: this.customer_data.customer_bank_name,
        edit_customer_bank_acc: this.customer_data.customer_bank_acc,
      };
      await axios
        .post(`/customer/dataedit/${this.$route.params.id}`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          this.reloadpage();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async delCustomerCar(item) {
      let payload = {
        car_id: item.id,
      };
      await axios
        .post(`/customer/cardel`, payload, {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((res) => {
          if (res.data.status === "car_delete") {
            this.reloadpage();
          } else {
            this.showWarrningBlock(false);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async regCustomerCar() {
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
          this.reloadpage();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async regCustomerData() {
      let payload = {
        customer_type: this.customer_type,
        customer_number: this.customer_number,
        customer_street: this.customer_street,
        customer_bank_name: this.customer_bank_name,
        customer_bank_acc: this.customer_bank_acc,
      };
      await axios
        .post(`/customer/custtype/${this.$route.params.id}`, payload, {
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
    showEditBlock(check) {
      this.showEdit = !check;
    },
    showDataFormBlock(check) {
      this.showDataForm = !check;
    },
    showWarrningBlock(check) {
      this.showWarrning = !check;
    },
    showCarWarrningBlock(check) {
      this.showCarWarrning = !check;
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