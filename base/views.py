from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Product
from .serializer import ProductSerializer

# Create your views here.


def index(req):
    return JsonResponse('HELLO ELY FROM VIEWS', safe=False)

def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)