from django.urls import path
from . import views

app_name = 'products'  # ADD THIS

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('list/', views.product_list, name='product_list'),
]


