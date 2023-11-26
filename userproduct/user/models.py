# models.py

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    preference = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    tags = models.TextField()

    def __str__(self):
        return self.product_name
