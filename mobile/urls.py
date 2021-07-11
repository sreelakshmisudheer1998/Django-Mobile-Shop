from django.urls import path
from .views import create_product, list_products, edit_item, add_brand, list_brand, update_brand,\
    product_detail, delete_brand, index,delete_product

urlpatterns = [
    path('addbrand', add_brand, name='add_brand'),
    path('listbrand', list_brand, name='list_brand'),
    path('updatebrand/<int:id>', update_brand, name='update_brand'),
    path('index', index, name='index'),
    path('brands/delete/<int:id>', delete_brand, name='delete_brand'),
    path("products", create_product, name="create_product"),
    path("list", list_products, name="fetchitems"),
    path("list/change/<int:id>", edit_item, name="edit_item"),
    path("list/<int:id>", product_detail, name="product_detail"),
    path("list/remove/<int:id>",delete_product, name="delete_product"),
]
