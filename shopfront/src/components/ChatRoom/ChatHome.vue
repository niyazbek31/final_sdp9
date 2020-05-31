<template>
<div>
     <header class="section-header">
    <section class="header-main border-bottom">
        <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-2 col-6">
            <a  @click="goHome" href="#" class="brand-wrap">
                <img class="logo" src="../../assets/logo.png" alt="Логотип"><!--================================================ -->
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
    // import Room from '@/components/rooms/Room.vue'
    // import Dialog from '@/components/rooms/Dialog.vue'

    export default {
        name: "Home",
        // components: {
        //     Room,
        //     Dialog
        // },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false,
                }
            }
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            // Открываю диалог
            // openDialog(id) {
                // this.dialog.id = id
                // this.dialog.show = true
            // }
        },
    }
</script>

<style scoped>

</style>
