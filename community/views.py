from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def community_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Get all posts (latest first)
    return render(request, 'community/community.html', {'posts': posts})

def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign logged-in user as author
            post.save()
            return redirect('community_home')  # FIX: Redirect must match the URL name
    else:
        form = BlogPostForm()

    return render(request, 'community/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  # FIX: Use 'BlogPost' instead of 'Post'
    return render(request, "community/post_detail.html", {"post": post})


