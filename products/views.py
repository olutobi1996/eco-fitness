from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .forms import ReviewForm, ProductForm
from .models import Product, Category, Review

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = request.GET.get('q', '')
    categories = request.GET.getlist('category')
    sort = request.GET.get('sort')
    direction = request.GET.get('direction')

    # Sorting logic
    if sort:
        sortkey = sort
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        if sortkey == 'category':
            sortkey = 'category__name'
        if direction == 'desc':
            sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    # Filtering by category
    if categories:
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    # Search logic
    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)
    elif 'q' in request.GET:
        messages.error(request, "You didn't enter any search criteria!")
        return redirect(reverse('products:all_products'))

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories if categories else None,
        'current_sorting': f'{sort}_{direction}' if sort else None,
    }

    return render(request, 'products/products.html', context)


def product_reviews(request, product_id=None):
    """ Render reviews and allow users to submit a review, including a product search """

    if product_id:
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product).order_by('-created_at')
    else:
        product = None
        reviews = []

    # Handle the search query
    query = request.GET.get('search', '').strip()  # Get the search query from the URL
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()  # Show all products if no search term is provided
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to leave a review.")
            return redirect('account_login')

        if not product:
            messages.error(request, "Please select a product to review.")
            return redirect(reverse('products:product_reviews'))  

        existing_review = Review.objects.filter(product=product, user=request.user).first()
        if existing_review:
            messages.error(request, "You've already left a review for this product.")
            return redirect(reverse('products:product_reviews_by_id', args=[product.id]))  

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been submitted!")
            return redirect(reverse('products:product_reviews_by_id', args=[product.id]))  
        else:
            messages.error(request, "There was an error with your review. Please check your input.")
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'products': products,  
    }

    return render(request, "products/reviews.html", context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:all_products'))

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to leave a review.")
            return redirect('account_login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been submitted!")
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.error(request, "There was an error with your review. Please check your input.")
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


def shop_view(request):
    """ A view to display the shop homepage with featured products, categories, and bundles. """
    featured_products = Product.objects.filter(is_featured=True)  
    categories = Category.objects.all()

    context = {
        "featured_products": featured_products,
        "categories": categories,
    }

    return render(request, "products/shop.html", context)

def category_products(request, category_slug):
    """ Display products for a specific category """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, "products/category_products.html", {
        "category": category,
        "products": products,
    })























