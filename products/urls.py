from django.urls import path

from .views import (
    add_product,
    all_products,
    category_products,
    delete_product,
    delete_review,
    edit_product,
    edit_review,
    product_detail,
    product_reviews,
    shop_view,
)

app_name = "products"

urlpatterns = [
    path("", all_products, name="all_products"),
    path("shop/", shop_view, name="shop"),
    path("<int:product_id>/", product_detail, name="product_detail"),
    path("add/", add_product, name="add_product"),
    path("edit/<int:product_id>/", edit_product, name="edit_product"),
    path("delete/<int:product_id>/", delete_product, name="delete_product"),
    path("reviews/", product_reviews, name="product_reviews"),
    path(
        "<int:product_id>/reviews/",
        product_reviews,
        name="product_reviews_by_id",
    ),
    path("reviews/edit/<int:review_id>/", edit_review, name="edit_review"),
    path("reviews/delete/<int:review_id>/",
         delete_review, name="delete_review"),
    path(
        "category/<slug:category_slug>/",
        category_products,
        name="category_products",
    ),
]
