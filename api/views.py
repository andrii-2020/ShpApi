from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer
import requests
from .confS import *


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__id=category)
        return queryset

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class PostTo(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        message = f'''       Новий Заказ\n
        Імя: {data['f_name']}\n 
        Фамілія: {data['f_name']}\n
        Телефон: {data['phone']}\n
        Продукт: {data['name_product']}\n
        Колір: {data['color_product']}\n
        Розмір: {data['size_product']}\n
        Ціна: {data['price_product']}\n
        '''
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.post(url)
        return Response(data)
        