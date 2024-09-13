from django.urls import path

from . import views

urlpatterns = [
    path('api/products/', views.ListProduct.as_view()),
    path('api/products_create/', views.CreateProduct.as_view()),
    path('shop/products_create/', views.CreateProductTemplate.as_view()),
]