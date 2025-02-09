from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
