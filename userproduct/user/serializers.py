# authentication/serializers.py

from rest_framework import serializers
from .models import Customer, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "age", "gender", "location", "preference"]
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "category", "description", "tags"]
        extra_kwargs = {"id": {"read_only": True}}
