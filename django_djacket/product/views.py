from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class LeatestProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    