from django.urls import path
from .views import (
    CreateImage,
    PostTo,
    CategoryList,
    ProductList,
    CategoryDetail,
    ProductDetail
)


urlpatterns = [
   path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/image/<int:pk>/', CreateImage.as_view(), name='CreateImage-detail'),
    path('sms/', PostTo.as_view(), name='CreateImage-detail'),
]