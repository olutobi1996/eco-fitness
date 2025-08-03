from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogPostForm
from .models import BlogPost
import logging


def community_home(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "community/community.html", {"posts": posts})



logger = logging.getLogger(__name__)

@login_required
def create_post(request):
    if request.method == "POST":
        logger.info("Received POST request for blog post creation")
        logger.info("FILES received: %s", request.FILES)

        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():  
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            logger.info("IMAGE FIELD: %s", post.image)
            logger.info("IMAGE NAME: %s", post.image.name)
            logger.info("IMAGE URL: %s", post.image.url)

            return redirect("community")
        else:
            logger.warning("Form is invalid: %s", form.errors)
    else:
        form = BlogPostForm()

    return render(request, "community/create_post.html", {"form": form})




def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "community/post_detail.html", {"post": post})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user != post.author:
        return redirect("community")

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = BlogPostForm(instance=post)

    return render(request, "community/edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user != post.author:
        return redirect("community")

    if request.method == "POST":
        post.delete()
        return redirect("community")

    return render(request, "community/delete_post.html", {"post": post})
