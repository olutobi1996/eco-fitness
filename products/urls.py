from django.urls import path
from . import views

app_name = 'products'  # Added for namespacing

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]



