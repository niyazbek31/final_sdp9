<template>

<div>
    <header class="section-header">
        <nav class="navbar navbar-dark navbar-expand p-0 bg-primary">
            <div class="container">
                <ul class="navbar-nav d-none d-md-flex mr-auto">
                    <li class="nav-item"><a class="nav-link" href="#">Главная</a></li>
                    <li class="nav-item"><a @click="goContact" class="nav-link" href="#">Контакты</a></li>
                    <li class="nav-item"><a @click="goChat" class="nav-link" href="#">Обсуждение</a></li>
                </ul>
                <ul class="navbar-nav">
                    <li  class="nav-item"><a href="#" class="nav-link"> Тел. номер: +7 777 777 77 77 </a></li>
                    <li class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Руский</a>
                        <ul class="dropdown-menu dropdown-menu-right" style="max-width: 100px;">
                            <li><a class="dropdown-item" href="#">Қазақша</a></li>
                            <li><a class="dropdown-item" href="#">English</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </nav>
        
        <section class="header-main border-bottom">
	        <div class="container">
                <div class="row align-items-center">
	                <div class="col-lg-2 col-6">
                        <a href="#" class="brand-wrap">
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
                                <a @click="goProfile" class="icon icon-sm rounded-circle border"><i class="fa fa-user"></i></a>
                                <div class="text">
                                    <span class="text-muted">Добро пожаловать!</span>
                                    <div v-if="!auth">
                                        <a @click="goLogin" href="#">Войти</a> |
                                        <a @click="goRegister" href="#">Регистрация</a>
                                    </div>
                                    <div v-if="auth">
                                        <a @click="logout" href="">Выйти</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
	        </div>
        </section>
    </header>
    <header>
        <nav class="navbar navbar-main navbar-expand-lg navbar-light border-bottom">
        <div class="container">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main_nav" aria-controls="main_nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="main_nav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link pl-0" @click="goCategory" href="#"><strong> <i class="fa fa-bars"></i> Категория</strong></a>
                <!--<a class="nav-link pl-0" data-toggle="dropdown" href="#"><strong> <i class="fa fa-bars"></i> Категория</strong></a>
                <div class="dropdown-menu">
                    <a class="dropdown-item" href="#">1</a>
                    <a class="dropdown-item" href="#">2</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">1</a>
                    <a class="dropdown-item" href="#">2</a>
                    <a class="dropdown-item" href="#">3</a>
                </div>-->
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Кухонный инвертарь</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Обои</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Инструменты</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Двери  Замки</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Стройматерилы</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Электротовары</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Хранение</a>
                </li>
            </ul>
            </div>
        </div>
        </nav>
    </header>

    <!-- ========================= SECTION INTRO ========================= -->
        <section class="section-intro padding-y-sm">
            <div class="container">
                <div class="intro-banner-wrap text-md-center">
                    <img style="width: 1000px; height: 200px;" src="../assets/banner.jpg" alt="Здесь будет слайдер или какой то баннер" class="img-fluid rounded">
                </div>
            </div>
        </section>
    <!-- ========================= SECTION INTRO END ========================= -->


    <!-- ========================= SECTION FEATURE ========================= -->
        <section class="section-content padding-y-sm">
        <div class="container">
            <article class="card card-body">
                <div class="row">
                    <div class="col-md-4">
                        <figure class="item-feature">
                            <span class="text-primary"><i class="fa fa-2x fa-truck"></i></span>
                            <figcaption class="pt-3">
                                <h5 class="title">Быстрая доставка</h5>
                                <p></p>
                            </figcaption>
                        </figure>
                    </div>
                    <div class="col-md-4">
                        <figure  class="item-feature">
                            <span class="text-primary"><i class="fa fa-2x fa-landmark"></i></span>
                            <figcaption class="pt-3">
                                <h5 class="title">Креативная стратегия</h5>
                                <p></p>
                            </figcaption>
                        </figure>
                    </div>
                    <div class="col-md-4">
                        <figure  class="item-feature">
                            <span class="text-primary"><i class="fa fa-2x fa-lock"></i></span>
                            <figcaption class="pt-3">
                                <h5 class="title">Высокий уровень безопасности</h5>
                                <p></p>
                            </figcaption>
                        </figure>
                    </div>
                </div>
            </article>
        </div>
        </section>
    <!-- ========================= SECTION FEATURE END ========================= -->


    <!-- ========================= SECTION CONTENT ========================= -->
        <section class="section-content">
            <div class="container">
                <header class="section-heading">
                    <h3 class="section-title">Популярнные товары</h3>
                </header>
                <div class="row">
                <!-- 1 -->
                    <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>
                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">17900.00 тг</div>
                                </figcaption>
                            </div>
                        </div>
                    <!-- 2 -->
                    <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>

                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">28000.00 тг</div>
                                </figcaption>
                            </div>
                        </div>

                        <!-- 1 -->
                        <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>
                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">17900.00 тг</div>
                                </figcaption>
                            </div>
                        </div>
                    <!-- 2 -->
                    <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>

                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">28000.00 тг</div>
                                </figcaption>
                            </div>
                        </div>
                </div>
            </div>
        </section>
    <!-- ========================= SECTION CONTENT END// ========================= -->

    <!-- ========================= SECTION CONTENT ========================= -->
        <section class="section-content">
            <div class="container">
                <header class="section-heading">
                    <h3 class="section-title">Новинки</h3>
                </header>
                <div class="row">
                <!-- 1 -->
                    <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>
                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">17900.00 тг</div>
                                </figcaption>
                            </div>
                        </div>
                    <!-- 2 -->
                        <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>

                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">28000.00 тг</div>
                                </figcaption>
                            </div>
                        </div>

                        <!-- 1 -->
                        <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>
                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">17900.00 тг</div>
                                </figcaption>
                            </div>
                        </div>
                    <!-- 2 -->
                    <div class="col-md-3">
                            <div href="#" class="card card-product-grid">
                                <a href="#" class="img-wrap"> <img src=""> </a>
                                <figcaption class="info-wrap">
                                    <a href="#" class="title">Название</a>

                                    <div class="rating-wrap">
                                        <ul class="rating-stars">
                                            <li style="width:80%" class="stars-active">
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                            <li>
                                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                            </li>
                                        </ul>
                                        <span class="label-rating text-muted"> 34 отзыв</span>
                                    </div>
                                    <div class="price mt-1">28000.00 тг</div>
                                </figcaption>
                            </div>
                        </div>
                </div>

            </div>
        </section>
    <!-- ========================= SECTION CONTENT END// ========================= -->

    <!-- ========================= SECTION CONTENT ========================= -->
        <section class="section-content padding-bottom-sm">
            <div class="container">
                <header class="section-heading">
                    <a href="#" class="btn btn-outline-primary float-right">Посмотреть все</a>
                    <h3 class="section-title">Рекомендация</h3>
                </header>
                <div class="row">
                <!-- 1 -->
                <div class="col-md-3">
                        <div href="#" class="card card-product-grid">
                            <a href="#" class="img-wrap"> <img src=""> </a>
                            <figcaption class="info-wrap">
                                <a href="#" class="title">Название</a>
                                <div class="rating-wrap">
                                    <ul class="rating-stars">
                                        <li style="width:80%" class="stars-active">
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                        <li>
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                    </ul>
                                    <span class="label-rating text-muted"> 34 отзыв</span>
                                </div>
                                <div class="price mt-1">17900.00 тг</div>
                            </figcaption>
                        </div>
                    </div>
                <!-- 2 -->
                    <div class="col-md-3">
                        <div href="#" class="card card-product-grid">
                            <a href="#" class="img-wrap"> <img src=""> </a>
                            <figcaption class="info-wrap">
                                <a href="#" class="title">Название</a>

                                <div class="rating-wrap">
                                    <ul class="rating-stars">
                                        <li style="width:80%" class="stars-active">
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                        <li>
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                    </ul>
                                    <span class="label-rating text-muted"> 34 отзыв</span>
                                </div>
                                <div class="price mt-1">28000.00 тг</div>
                            </figcaption>
                        </div>
                    </div>

                    <!-- 1 -->
                    <div class="col-md-3">
                        <div href="#" class="card card-product-grid">
                            <a href="#" class="img-wrap"> <img src=""> </a>
                            <figcaption class="info-wrap">
                                <a href="#" class="title">Название</a>
                                <div class="rating-wrap">
                                    <ul class="rating-stars">
                                        <li style="width:80%" class="stars-active">
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                        <li>
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                    </ul>
                                    <span class="label-rating text-muted"> 34 отзыв</span>
                                </div>
                                <div class="price mt-1">17900.00 тг</div>
                            </figcaption>
                        </div>
                    </div>
                <!-- 2 -->
                <div class="col-md-3">
                        <div href="#" class="card card-product-grid">
                            <a href="#" class="img-wrap"> <img src=""> </a>
                            <figcaption class="info-wrap">
                                <a href="#" class="title">Название</a>

                                <div class="rating-wrap">
                                    <ul class="rating-stars">
                                        <li style="width:80%" class="stars-active">
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                        <li>
                                            <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                                        </li>
                                    </ul>
                                    <span class="label-rating text-muted"> 34 отзыв</span>
                                </div>
                                <div class="price mt-1">28000.00 тг</div>
                            </figcaption>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    <!-- ========================= SECTION CONTENT END// ========================= -->

    <!-- ========================= SECTION  ========================= -->
        <section class="section-name bg padding-y-sm">
        <div class="container">
        <header class="section-heading">
            <h3 class="section-title">Бренды</h3>
        </header>

        <div class="row">
            <div class="col-md-2 col-6">
                <figure class="box item-logo">
                    <a href="#"><img src=""></a>
                    <figcaption class="border-top pt-2">BOSCH</figcaption>
                </figure>
            </div>
            <div class="col-md-2  col-6">
                <figure class="box item-logo">
                    <a href="#"><img src=""></a>
                    <figcaption class="border-top pt-2">KNAUF</figcaption>
                </figure>
            </div>
            <div class="col-md-2  col-6">
                <figure class="box item-logo">
                    <a href="#"><img src=""></a>
                    <figcaption class="border-top pt-2">IKEA</figcaption>
                </figure>
            </div>
            <div class="col-md-2  col-6">
                <figure class="box item-logo">
                    <a href="#"><img src=""></a>
                    <figcaption class="border-top pt-2">HAMMER</figcaption>
                </figure>
            </div>
            <div class="col-md-2  col-6">
                <figure class="box item-logo">
                    <a href="#"><img src=""></a>
                    <figcaption class="border-top pt-2">IDDIS</figcaption>
                </figure>
            </div>
            <div class="col-md-2  col-6">
                <figure class="box item-logo">
                    <a href="#"><img src=""></a>
                    <figcaption class="border-top pt-2">LUMINARC</figcaption>
                </figure>
            </div>
        </div>
        </div>
        </section>
    <!-- ========================= SECTION  END// ========================= -->

    <!-- ========================= FOOTER ========================= -->
        <footer class="section-footer border-top bg">
            <div class="container">
                <section class="footer-top  padding-y">
                    <div class="row">
                        <aside class="col-md col-6">
                            <h6 class="title">Бренды</h6>
                            <ul class="list-unstyled">
                                <li> <a href="#">Knauf</a></li>
                    <li> <a href="#">Bosch</a></li>
                                <li> <a href="#">Hammer</a></li>
                                <li> <a href="#">Iddis</a></li>
                            </ul>
                        </aside>
                        <aside class="col-md col-6">
                            <h6 class="title">Компания</h6>
                            <ul class="list-unstyled">
                                <li> <a href="#">О нас</a></li>
                                <li> <a href="#">Вакансия</a></li>
                                <li> <a href="#">===</a></li>
                                <li> <a href="#">===</a></li>
                                <li> <a href="#">===</a></li>
                            </ul>
                        </aside>
                        <aside class="col-md col-6">
                            <h6 class="title">Помощь</h6>
                            <ul class="list-unstyled">
                                <li> <a href="#">Контакты</a></li>
                                <li> <a href="#">===</a></li>
                                <li> <a href="#">===</a></li>
                                <li> <a href="#">===</a></li>
                                <li> <a href="#">===</a></li>
                            </ul>
                        </aside>
                        <aside class="col-md col-6">
                            <h6 class="title">Аккаунт</h6>
                            <ul class="list-unstyled">
                                <li> <a href="#">Войти</a></li>
                                <li> <a href="#">Регистрация</a></li>
                                <li> <a href="#">Настройка аккаунт</a></li>
                                <li> <a href="#">Мои заказы</a></li>
                            </ul>
                        </aside>
                        <aside class="col-md">
                            <h6 class="title">Мы на социальных сетях</h6>
                            <ul class="list-unstyled">
                                <li><a href="#"> <i class="fab fa-facebook"></i> Facebook </a></li>
                                <li><a href="#"> <i class="fab fa-twitter"></i> Twitter </a></li>
                                <li><a href="#"> <i class="fab fa-instagram"></i> Instagram </a></li>
                                <li><a href="#"> <i class="fab fa-youtube"></i> Youtube </a></li>
                            </ul>
                        </aside>
                    </div>
                </section>

                <section class="footer-bottom row">
                    <div class="col-md-2">
                        <p class="text-muted"> 2020 </p>
                    </div>
                    <div class="col-md-8 text-md-center">
                        <span  class="px-2">name@name.kz</span>
                        <span  class="px-2">+7 777 777 77 77</span>
                        <span  class="px-2">Адрес</span>
                    </div>
                    <div class="col-md-2 text-md-right text-muted">
                        <i class="fab fa-lg fa-cc-visa"></i>
                        <i class="fab fa-lg fa-cc-paypal"></i>
                        <i class="fab fa-lg fa-cc-mastercard"></i>
                    </div>
                </section>
            </div>
        </footer>
    <!-- ========================= FOOTER ========================= -->
</div>
</template>\

<script>
import $ from 'jquery'

    export default {
        name: "Home",
        computed: {
            auth(){
                if(sessionStorage.getItem("auth_token")){
                    return true
                }
            }
        },
        methods: {
            goLogin(){
                this.$router.push({name: "login"})
            },
            goChat(){
                this.$router.push({name: "chathomr"})
            },
            goContact(){
                this.$router.push({name: "contact"})
            },
            goRegister(){
                this.$router.push({name: "register"})
            },
            goCategory(){
                this.$router.push({name: "category"})
            },
            goProfile(){
                this.$router.push({name: "profile"})
            },
            logout(){
                sessionStorage.removeItem("auth_token")
            }
        }
    }
</script>

<style scoped>

</style>
