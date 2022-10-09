<template>
  <section class="container">
    <div class="columns">
      <div class="column is-one-fifth">
        <aside class="menu">
          <p class="menu-label">Options</p>
          <ul class="menu-list">
            <li><router-link to="/dashboard">Lietotājs</router-link></li>
            <li>
              <router-link to="/dashboard/customerreg">Registrēt klientu</router-link>
            </li>
            <li>
              <router-link to="/dashboard/workerreg">Registrēt darbinieku</router-link>
            </li>
            <li>
              <router-link to="/dashboard/customers">Klienti</router-link>
            </li>
            <li>
              <router-link to="/dashboard/customerreg">Veicamie darbi</router-link>
            </li>
          </ul>
        </aside>
      </div>
      <div class="column">
        <router-view />
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "UserDashboard",
};
</script>