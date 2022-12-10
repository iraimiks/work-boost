<template>
  <section class="container">
    <hr>
    <div class="columns" >
      <div class="column is-one-fifth" id="nav-left">
        <aside class="menu">
          <p class="menu-label">Lietotāja darbs</p>
          <ul class="menu-list">
            <li>
              <router-link
                to="/dashboard"
                >Lietotājs</router-link
              >
            </li>
          </ul>
        </aside>
        <aside class="menu">
          <p class="menu-label">Registrācija</p>
          <ul class="menu-list">
            <li>
              <router-link
                to="/dashboard/customerreg"
                >Registrēt klientu</router-link
              >
            </li>
            <li>
              <router-link to="/dashboard/workerreg"
                >Registrēt darbinieku</router-link
              >
            </li>
          </ul>
        </aside>
        <aside class="menu">
          <p class="menu-label">Meklēt</p>
          <ul class="menu-list">
            <li>
              <router-link to="/dashboard/customers">Klienti</router-link>
            </li>
            <li>
              <router-link to="/dashboard/workers">Darbinieki</router-link>
            </li>
            <li>
              <router-link to="/dashboard/cars">Auto saraksts</router-link>
            </li>
          </ul>
        </aside>
        <aside class="menu">
          <p class="menu-label">Veicamie darbi</p>
          <ul class="menu-list">
            <li>
              <router-link to="/dashboard/inwork"
                >Visi darbi ar auto</router-link
              >
            </li>
          </ul>
        </aside>
      </div>
      <div class="column">
        <hr>
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
<style>
#nav-left .active-class {
  background: rgba(0, 51, 255, 0.637);
  color: white;
}
</style>