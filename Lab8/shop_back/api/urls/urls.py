from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("products/", include("api.urls.product")),
    path("categories/", include("api.urls.category")),
]
