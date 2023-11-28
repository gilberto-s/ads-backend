from django.shortcuts import render
from django.http import Http404

from .models import Product

def index(request):
  product_list = Product.objects.order_by("id")
  context = {
     "product_list": product_list,
  }
  return render(request, "paes/index.html", context)


def detail(request, product_id):
    try:
       product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
       raise Http404("Produto não existe")
    return render(request, "paes/detail.html", { "product": product })
