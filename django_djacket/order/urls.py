from django.urls import path, include
from .views import *

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('orders/', OrderList.as_view(), name='orders'),
    
] 