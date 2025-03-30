from django.urls import path

from api.views.category_products import CategoryProductView
from api.views.category import CategoryView

urlpatterns = [
    path("", CategoryView.as_view()),
    path("<int:id_>/", CategoryView.as_view()),
    path("<int:id_>/products/", CategoryProductView.as_view()),
]
