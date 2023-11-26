# views.py

from rest_framework import generics

from django.http import JsonResponse
from django.apps import apps
from .models import Transaction

# from userproduct.user.models import Customer
from .serializers import TransactionSerializer


class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user_transactions = Transaction.objects.filter(user_id=user_id).values(
            "user", "product"
        )
        product_model = apps.get_model("user", "Product")
        products = list(
            product_model.objects.filter(
                id__in=[row["product"] for row in user_transactions]
            ).values()
        )
        #    data = list(SomeModel.objects.values())
        print(products)
        print(dir(products))
        return JsonResponse(products, safe=False)


class CreateTransaction(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        customer_model = apps.get_model("user", "Customer")
        user = customer_model.objects.filter(id=self.kwargs["user_id"]).first()
        serializer.save(user=user)


def get_dataset(_, user_id):
    user_transactions = Transaction.objects.filter(user_id=user_id).values(
        "user", "product"
    )
    customer_model = apps.get_model("user", "Customer")
    product_model = apps.get_model("user", "Product")
    cust = customer_model.objects.filter(id=user_id)
    products = product_model.objects.filter(
        id__in=[row["product"] for row in user_transactions]
    )
    product_data = list(
        products.values("category", "product_name", "description", "tags")
    )
    cust_data = list(cust.values("id", "name", "preference"))

    data = []
    for each_data in product_data:
        each_data.update(cust_data[0])
        data.append(each_data)

    return JsonResponse(data, safe=False)
