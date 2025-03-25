from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def community_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'community/community.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('community')
    else:
        form = BlogPostForm()
    return render(request, 'community/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "community/post_detail.html", {"post": post})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user != post.author:
        return redirect('community')  

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'community/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user != post.author:
        return redirect('community')  

    if request.method == "POST":
        post.delete()
        return redirect('community')

    return render(request, 'community/delete_post.html', {'post': post})


