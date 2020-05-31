from django.db import models

from django.contrib.auth.models import User
# from djoser.urls.base import User


"""======================  Chat ======================="""
class Room(models.Model):
    """Модель комнаты чата"""
    creater = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    """Модель чата"""
    room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"




"""==========================Product=============================="""

class Category(models.Model):
    """Модель категория"""
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"
    def __str__(self):
        return self.name

class Products(models.Model):
    """Модель Продукт"""
    category_id = models.ForeignKey(Category, related_name='category', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    details = models.CharField(max_length=100, null=False, default='', verbose_name="Характеристика")
    link_img = models.ImageField(blank=False, null=True, verbose_name="Картинки")
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    def __str__(self):
        return self.name


""" ========= Products ===============================
class Products(models.Model):
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    details = models.CharField(max_length=100, null=False, default='', verbose_name="Характеристика")
    link_img = models.ImageField(blank=False, null=True, verbose_name="Картинки")
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'
    def __str__(self):
        return self.name
"""
""" ========= Category ==========================
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    products = models.ManyToManyField(Products, verbose_name="Продукты", related_name="cat_of_pro")
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
    def __str__(self):
        return self.name
"""
