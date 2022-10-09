<template>
  <table class="table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Vārds</th>
        <th>Izveides datums</th>
        <th>Darbības</th>
      </tr>
    </thead>
    <tbody>
        <tr v-for="item in items" v-bind:key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.create_date }}</td>
          <td>
            <router-link :to="'/dashboard/customers/' + item.id "
              >Pāriet</router-link
            >
          </td>
        </tr>
      </tbody>
  </table>
</template>
<script>
export default {
    name: 'UserViewTable',
    props: {
        items: Array,
    }
};
</script>