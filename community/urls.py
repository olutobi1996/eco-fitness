from django.urls import path
from . import views

urlpatterns = [
    path("", views.community_home, name="community"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("create/", views.create_blog_post, name="create_post"),  
    path("post/<int:post_id>/edit/", views.edit_post, name="edit_post"),
    path("post/<int:post_id>/delete/", views.delete_post, name="delete_post"),
]
