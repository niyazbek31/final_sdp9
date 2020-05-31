# coding=utf-8
from django.urls import path
from main.views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/', Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),
    path('category/', CategoryViews.as_view()),
    path('products/', ProductsViews.as_view()),

]
