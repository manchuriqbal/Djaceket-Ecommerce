from django.urls import path, include
from .views import LeatestProductList

urlpatterns = [
    path('leatest-products/', LeatestProductList.as_view()),
] 