# urls.py

from django.urls import path
from .views import CreateTransaction, get_dataset

urlpatterns = [
    path(
        "create-transaction/<int:user_id>/",
        CreateTransaction.as_view(),
        name="create-transaction",
    ),
    path("get_dataset/<int:user_id>/", get_dataset),
]
