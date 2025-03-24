from django.urls import path
from .views import community_home, create_post, post_detail

urlpatterns = [
    path("", community_home, name="community"),  
    path("create-post/", create_post, name="create_post"),  
    path("post/<int:post_id>/", post_detail, name="post_detail"),  
]

