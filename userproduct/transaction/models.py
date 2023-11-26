# models.py

from django.db import models

# from ..user.models import Customer


class Transaction(models.Model):
    user = models.ForeignKey("user.Customer", on_delete=models.CASCADE)
    product = models.ForeignKey("user.Product", on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.product.product_name}"
