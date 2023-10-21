from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    category_list = Category.objects.all()
    return render(
        request,
        "store/product_list.html",
        context={"product_list": products, "category_list": category_list},
    )


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    category_list = Category.objects.all() 
    return render(
        request,
        "store/product_detail.html",
        context={"product": product, "category_list": category_list},
    )
