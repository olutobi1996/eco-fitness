from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ReviewForm  
from .models import Product, Category, Bundle

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
        return redirect(reverse('all_products'))

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories if categories else None,
        'current_sorting': f'{sort}_{direction}' if sort else None,
    }

    return render(request, 'products/products.html', context)

def product_reviews(request, product_id):
    """ Render reviews and allow users to submit a review """
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
            return redirect('product_reviews', product_id=product.id)
        else:
            messages.error(request, "There was an error with your review. Please check your input.")

    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,  
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
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {'form': form}
    return render(request, template, context)

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

    template = 'products/edit_product.html'
    context = {'form': form, 'product': product}
    return render(request, template, context)

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

def product_list(request):
    """ A simple product list view """
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

def product_reviews(request, product_id):
    """ Render reviews and allow users to submit a review """
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
            return redirect('products:product_detail', product_id=product.id)
        else:
            messages.error(request, "There was an error with your review. Please check your input.")

    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,  
    }

    return render(request, "products/product_detail.html", context)


def reviews(request):
    context = {} 
    return render(request, "products/reviews.html", context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


def shop_view(request):
    """ A view to display the shop homepage with featured products, categories, and bundles. """
    featured_products = Product.objects.filter(is_featured=True)  # ✅ This will now work
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

    context = {
        "category": category,
        "products": products,
    }

    return render(request, "products/category_products.html", context)











