from django.urls import path
from .views import upload_product,product_list,product_details,add_to_cart,edit_product_view
# from django.shortcuts import redirect

urlpatterns = [path("products/upload",upload_product,name = "product_update_view"),
               path("products/product_list",product_list,name = "product_list"),
               path("products/<int:id>",product_details,name="product_details_view"),
               path("products/add_to_cart", add_to_cart, name="add_to_cart_view"),
               path("products/edit/<int:id>",edit_product_view,name="product_edit_view"),
               ]

