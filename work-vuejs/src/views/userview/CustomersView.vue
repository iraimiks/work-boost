<template>
  <div>
    <h2 class="title">Reģistrēti klienti</h2>
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
      <tbody>
        <tr v-for="item in items" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.phone }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/dashboard/customers/' + item.id"
              >Klienta lapa</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
    <nav class="pagination" role="navigation" aria-label="pagination">
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
          <a class="pagination-link" v-bind:class="{ 'is-current': coloring === n }" @click="currentPageEvent(n)">{{
            n
          }}</a>
        </li>
        <li v-bind:class="{ 'block-show': !showLastNumber }">
          <a class="pagination-link"  @click="currentPageEvent(pageCountShow)">{{ pageCountShow }} Pēdējā</a>
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
    };
  },
  mounted() {
    this.getCustomers();
  },
  computed: {},
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
      if (lens % 2 === 0) {
        this.pageCountShow = lens / 2;
      } else {
        this.pageCountShow = Math.round(lens / 2);
      }
      this.items = this.customers.slice((page - 1) * 2, page * 2);
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
      if(currentPage >= 4) {
        this.showFirstNumber = true;
      } else {
        this.showFirstNumber = false;
      }

      if(currentPage >= 5) {
        this.showLastNumber = false;
      } else {
        this.showLastNumber = true;
      }
    },

  },
};
</script>