# authentication/views.py

from rest_framework import generics
from .models import Customer, Product
from .serializers import UserSerializer, ProductSerializer


class UserProfileList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
