<template>
<div>
      <header class="section-header">
    <section class="header-main border-bottom">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-2 col-6">
            <a @click="goHome" class="brand-wrap">
              <img class="logo" src="../assets/logo.png" alt="Логотип"><!--================================================ -->
            </a>
          </div>
          <div class="col-lg-6 col-12 col-sm-12">
            <form action="#" class="search">
              <div class="input-group w-100">
                <input type="text" class="form-control" placeholder="Поиск">
                <div class="input-group-append">
                  <button class="btn btn-primary" type="submit">
                    <i class="fa fa-search"></i>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="widgets-wrap float-md-right">
              <div class="widget-header  mr-3">
                <a href="#" class="icon icon-sm rounded-circle border"><i class="fa fa-shopping-cart"></i></a>
                <span class="badge badge-pill badge-danger notify">0</span>
              </div>
              <div class="widget-header icontext">
                <a href="#" class="icon icon-sm rounded-circle border"><i class="fa fa-user"></i></a>
                <div class="text">
                  <span class="text-muted">Добро пожаловать!</span>
                  <div>
                    <a @click="goLogin" href="#">Войти</a> |
                        <a @click="goRegister" href="#">Регистрация</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </header>



  <!-- ========================= SECTION CONTENT ========================= -->
  <section class="section-content padding-y">

    <!-- ============================ COMPONENT REGISTER   ================================= -->
    <div class="card mx-auto" style="max-width:520px; margin-top:40px;">
      <article class="card-body">
        <header class="mb-4"><h4 class="card-title">Регистрация</h4></header>
        <form>
          <div class="form-row">
            <div class="col form-group">
              <label>Имя</label>
              <input type="text" class="form-control" placeholder="">
            </div>
            <div class="col form-group">
              <label>Фамилия</label>
              <input type="text" class="form-control" placeholder="">
            </div>
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" placeholder="">
            <small class="form-text text-muted">Мы никогда не передадим вашу электронную почту кому-либо еще. Ну посмотрим</small>
          </div>
          <div class="form-group">
            <label class="custom-control custom-radio custom-control-inline">
              <input class="custom-control-input" checked="" type="radio" name="gender" value="option1">
              <span class="custom-control-label"> муж. </span>
            </label>
            <label class="custom-control custom-radio custom-control-inline">
              <input class="custom-control-input" type="radio" name="gender" value="option2">
              <span class="custom-control-label"> жен.</span>
            </label>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label>Что то еще</label>
              <input type="text" class="form-control">
            </div>
            <div class="form-group col-md-6">
              <label>Город</label>
              <select id="inputState" class="form-control">
                <option> Выберите...</option>
                <option>Шымкент</option>
                <option>Астана</option>
                <option selected="">Алматы</option>
                <option>Актау</option>
                <option>Семей</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label>Придумайте пароль</label>
              <input class="form-control" type="password">
            </div>
            <div class="form-group col-md-6">
              <label>Повторите пароль</label>
              <input class="form-control" type="password">
            </div>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block"> Регистрация </button>
          </div>
          <div class="form-group">
            <label class="custom-control custom-checkbox"> <input type="checkbox" class="custom-control-input" checked=""> <div class="custom-control-label"> Я согласен типана все права <a href="#">какие та документы тут</a>  </div> </label>
          </div>
        </form>
      </article>
    </div>
    <p class="text-center mt-4">Есть аккаунт уау! круто!? <a href="">Заходи тогда ))</a></p>
    <br><br>
    <!-- ============================ COMPONENT REGISTER  END.// ================================= -->


  </section>
  <!-- ========================= SECTION CONTENT END// ========================= -->


  <!-- ========================= FOOTER ========================= -->
  <footer class="section-footer border-top padding-y">
    <div class="container">
      <p class="float-md-right">
         Copyright 2020 Ну типа все права защищены
      </p>
      <p>
        <a href="#">Просто так</a>
      </p>
    </div>
  </footer>
  <!-- ========================= FOOTER END // ========================= -->

</div>
</template>

<script>
  export default {
        name: 'Register',
        methods: {
            goLogin(){
                this.$router.push({name: "login"})
            },
            goRegister(){
                this.$router.push({name: "register"})
            },
            goHome(){
                this.$router.push({name: "home"})
            }
        }
    }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
