from rest_framework import serializers
from django.contrib.auth.models import User

from main.models import Room, Chat, Products, Category


"""======================Product======================="""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name")

class ProductsSerializer(serializers.ModelSerializer):
    link_img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Products
        fields = ("category_id","id","name","price","details","link_img")


"""===========================Chat==================================="""
class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ("id", "creater", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializer()
    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    class Meta:
        model = Chat
        fields = ("room", "text")
