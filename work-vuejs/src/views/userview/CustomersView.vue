<template>
  <div>
    <h2 class="title">Reģistrēti klienti</h2>
    <hr />
    <DataTable :columns="columns" :data="customers" class="table table-hover table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Vārds</th>
          <th>Talrunis</th>
          <th>Izveides datums</th>
        </tr>
      </thead>
    </DataTable>
  </div>
</template>
<script >
import axios from "axios";
import DataTable from "datatables.net-vue3";

export default {
  name: "CustomersView",
  components: { DataTable: DataTable },
  data() {
    return {
      customers: [],
      columns: [
        { data: "id" },
        {
          data: "name",
          render: function (data, type, row, meta) {
            if (type === "display") {
              data =
                '<a href="/dashboard/customers/' +
                row.id +
                '">' +
                data +
                "</a>";
            }
            return data;
          },
        },
        { data: "phone" },
        { data: "create_date" },
      ],
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
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
@import 'bootstrap';
@import 'datatables.net-bs5';
</style>