<template>
  <div>
    <h2 class="title">Auto</h2>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Meklēt</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input
              class="input"
              v-model="searchWord"
              type="text"
              placeholder="Meklēt auto reg. numuru"
            />
          </p>
        </div>
      </div>
    </div>
    <DataTable :columns="columns" :data="cars" class="table table-hover table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Auto numurs</th>
          <th>Auto marka</th>
          <th>Izveides datums</th>
        </tr>
      </thead>
    </DataTable>
  </div>
</template>
<script>
import axios from "axios";
import DataTable from "datatables.net-vue3";

export default {
  name: "AllCarsView",
  components: { DataTable: DataTable },
  data() {
    return {
      cars: [],
            columns: [
        { data: "id" },
        {
          data: "number",
          render: function (data, type, row, meta) {
            if (type === "display") {
              data =
                '<a href="/dashboard/customers/' +
                row.customer_id +
                '">' +
                data +
                "</a>";
            }
            return data;
          },
        },
        { data: "brand" },
        { data: "create_date" },
      ],
    };
  },
  computed: {},
  mounted() {
    this.getAllCars();
  },
  methods: {
    async getAllCars() {
      await axios
        .get("/customer/cars")
        .then((res) => {
          this.cars = res.data.cars;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
@import "bootstrap";
@import "datatables.net-bs5";
</style>