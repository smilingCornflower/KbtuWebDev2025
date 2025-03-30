from django.urls import path
from api.views.product import ProductView


urlpatterns = [
    path("", ProductView.as_view()),
    path("<int:id_>/", ProductView.as_view())
]
