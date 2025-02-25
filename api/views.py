from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer
import requests
from .confS import *


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__id=category)
        return queryset

class ProductDetail(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(pk=self.kwargs.get('pk'))
        return queryset



class CreateImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class PostTo(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        if self.request.data:
            message = f'''\nНовий Заказ\n
                    Імя: {data['f_name']}\n 
                    Фамілія: {data['f_name']}\n
                    Телефон: {data['phone']}\n
                    Місто/село: {data['city']}\n
                    Відділення нової пошти: {data['number_posts']}\n
                    Продукт: {data['name_product']}\n
                    Розмір: {data['size_product']}\n
                    Ціна: {data['price_product']}\n
                    '''

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            requests.post(url)

        return Response(data.request)
