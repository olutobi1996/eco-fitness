from django.urls import path

from subscriptions.views import plans_view

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.add_product, name="add_product"),
    path("plans/", plans_view, name="plans"),
    path("profile/", views.profile, name="profile"),
    path("cart/", views.cart, name="cart"),
]
