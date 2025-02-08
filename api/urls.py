from django.urls import path
from .views import (
    CategoryListCreate, 
    CategoryDetail, 
    ProductListCreate, 
    ProductDetail,
    CreateImage
)


urlpatterns = [
   path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/image/<int:pk>/', CreateImage.as_view(), name='CreateImage-detail'),
]