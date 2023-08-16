from django.urls import path, include
from .views import LeatestProductList, ProductDetails

urlpatterns = [
    path('leatest-products/', LeatestProductList.as_view()),
    path('product/<slug:category_slug>/<slug:product_slug>/', ProductDetails.as_view()),
] 