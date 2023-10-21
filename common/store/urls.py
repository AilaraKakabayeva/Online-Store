from django.urls import path
from .views import product_list, product_detail


urlpatterns = [
    path('', product_list, name="product_list_url"),  
    path('products/<int:pk>/', product_detail) 
]