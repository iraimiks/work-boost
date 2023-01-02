<template>
  <div>
    <h2 class="title">Reģistrēti klienti</h2>
    <hr>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Meklēt pēc vārda</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input
              class="input"
              v-model="searchWord"
              type="text"
              placeholder="Meklēt vārdu"
            />
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Meklēt pēc tel</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input
              class="input"
              v-model="searchTel"
              type="text"
              placeholder="Meklēt tel"
            />
          </p>
        </div>
      </div>
    </div>

    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Vārds</th>
          <th>Talrunis</th>
          <th>Izveides datums</th>
          <th>Darbības</th>
        </tr>
      </thead>
      <tbody v-if="searchType === 'name'">
        <tr v-for="item in filterCustomer" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.phone }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/dashboard/customers/' + item.id" class="button"
              >Klienta lapa</router-link
            >
          </td>
        </tr>
      </tbody>
      <tbody v-else-if="searchTel != ''">
        <tr v-for="item in filterTel" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.phone }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/dashboard/customers/' + item.id" class="button"
              >Klienta lapa</router-link
            >
          </td>
        </tr>
      </tbody>
      <tbody v-else>
        <tr v-for="item in items" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.phone }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/dashboard/customers/' + item.id" class="button"
              >Klienta lapa</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
    <nav
      class="pagination"
      role="navigation"
      aria-label="pagination"
      v-bind:class="{ 'block-show': searchWord != '' || searchTel != '' }"
    >
      <a
        class="pagination-previous"
        v-bind:class="{ 'is-disabled': stopLeft }"
        @click="caruselLeft()"
        >Pakreisi</a
      >
      <a
        class="pagination-next"
        v-bind:class="{ 'is-disabled': stopRight }"
        @click="caruselRight()"
        >Palabi</a
      >
      <ul class="pagination-list">
        <li v-bind:class="{ 'block-show': !showFirstNumber }">
          <a class="pagination-link" @click="currentPageEvent(1)">1 Sākums</a>
        </li>
        <li v-for="n in result" v-bind:key="n">
          <a
            class="pagination-link"
            v-bind:class="{ 'is-current': coloring === n }"
            @click="currentPageEvent(n)"
            >{{ n }}</a
          >
        </li>
        <li v-bind:class="{ 'block-show': !showLastNumber }">
          <a class="pagination-link" @click="currentPageEvent(pageCountShow)"
            >{{ pageCountShow }} Pēdējā</a
          >
        </li>
      </ul>
    </nav>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "CustomersView",
  data() {
    return {
      customers: [],
      items: [],
      pageCountShow: 0,
      pageCarusel: 1,
      stopRight: false,
      stopLeft: false,
      coloring: 1,
      result: [],
      showFirstNumber: false,
      showLastNumber: true,
      searchtype: "",
      search: "",
      searchWord: "",
      searchTel: "",
      itemsPerList: 5,
    };
  },
  mounted() {
    this.getCustomers();
  },
  computed: {
    filterCustomer() {
      return this.customers.filter((customer) => {
        return (
          customer.name.toLowerCase().indexOf(this.search.toLowerCase()) != -1
        );
      });
    },
    filterTel() {
      return this.customers.filter((customer) => {
        return customer.phone.indexOf(this.searchTel) != -1;
      });
    },
  },
  methods: {
    async getCustomers() {
      await axios
        .get("/customer/list")
        .then((res) => {
          this.customers = res.data.customers;
          this.getPages(1);
          this.currentPageEvent(1);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getPages(page) {
      let lens = this.customers.length;
      if (lens % this.itemsPerList === 0) {
        this.pageCountShow = lens / this.itemsPerList;
      } else {
        this.pageCountShow = Math.round(lens / this.itemsPerList);
      }
      this.items = this.customers.slice(
        (page - 1) * this.itemsPerList,
        page * this.itemsPerList
      );
    },
    currentPageEvent(num) {
      this.generatePageRange(num, this.pageCountShow);
      this.getPages(num);
    },
    caruselRight() {
      this.pageCarusel += 1;
      if (this.pageCarusel <= this.pageCountShow) {
        this.currentPageEvent(this.pageCarusel);
        this.stopLeft = false;
      } else {
        this.pageCarusel = this.pageCountShow;
        this.stopRight = true;
      }
    },
    caruselLeft() {
      this.pageCarusel -= 1;
      if (this.pageCarusel !== 0) {
        this.currentPageEvent(this.pageCarusel);
        this.stopRight = false;
      } else {
        this.stopLeft = true;
        this.pageCarusel = 1;
      }
    },
    generatePageRange(currentPage, pageCount) {
      this.coloring = currentPage;
      let delta = 2;
      let left = currentPage - delta;
      let right = currentPage + delta + 1;
      this.result = Array.from({ length: pageCount }, (v, k) => k + 1).filter(
        (i) => i && i >= left && i < right
      );
      if (currentPage >= 4) {
        this.showFirstNumber = true;
      } else {
        this.showFirstNumber = false;
      }

      if (currentPage >= 5) {
        this.showLastNumber = false;
      } else {
        this.showLastNumber = true;
      }
    },
  },
};
</script>