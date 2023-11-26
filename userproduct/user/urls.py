# authentication/urls.py

from django.urls import path
from .views import UserProfileList, UserProfileDetail, ProductList, ProductDetail

urlpatterns = [
    path("user-profiles/", UserProfileList.as_view(), name="user-profile-list"),
    path(
        "user-profiles/<int:pk>/",
        UserProfileDetail.as_view(),
        name="user-profile-detail",
    ),
    path("products/", ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
]
