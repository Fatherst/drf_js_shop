from rest_framework import generics
from django.views.generic.base import TemplateView
from .serializers import ProductSerializer
from .models import Product

class ListProduct(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CreateProductTemplate(TemplateView):
    template_name = 'index.html'