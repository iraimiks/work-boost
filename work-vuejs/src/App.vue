<template>
  <section class="hero is-large is-info">
    <div class="hero-body">
      <div class="container is-max-desktop">
        <div class="notification is-info">
          <div class="columns is-centered">
            <div class="column is-half">
              <form>
                <div class="field">
                  <label class="label">Lietotājs</label>
                  <div class="control">
                    <input class="input" type="text" placeholder="liet-xxxx" />
                  </div>
                </div>
                <div class="field">
                  <label class="label">Parole</label>
                  <div class="control">
                    <input
                      class="input"
                      type="password"
                      placeholder="Jūsu parole"
                    />
                  </div>
                </div>
                <div class="field">
                  <button class="button">Ienākt</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>