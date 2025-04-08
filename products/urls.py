from django.urls import path
from .views import (  
    all_products,
    product_detail,  
    add_product,
    edit_product,
    delete_product,
    product_reviews,  
    shop_view,  
    category_products,  
)

app_name = 'products'  

urlpatterns = [
    path('', all_products, name='all_products'),
    path("shop/", shop_view, name="shop"),  
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('<int:product_id>/reviews/', product_reviews, name='product_reviews'),  
    path("category/<slug:category_slug>/", category_products, name="category_products"),  
]












