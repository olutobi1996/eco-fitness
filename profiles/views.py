from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product, Category
from products.forms import ProductForm
from .forms import UserProfileForm
from checkout.models import Order 
from django.urls import reverse
from .models import UserProfile
from .forms import UserProfileForm
 
# Create your views here.

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

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

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
            return redirect(reverse('product_detail', args=[product.id]))
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
    return redirect(reverse('all_products'))

def product_list(request):
    """ A simple product list view """
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

@login_required
def profile(request):
    """ Display and update the user's profile """
    
    user_profile = get_object_or_404(UserProfile, username=request.user.username)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=user_profile)

   
    orders = Order.objects.filter(user_profile=user_profile).order_by('-created_at')

    print("User Profile Loaded:", user_profile)
    print("Orders Retrieved:", orders)

    context = {
        'user_profile': user_profile,  # Make sure this is passed to the template
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def edit_profile(request):
    """ Allow users to edit their profile details """
    user_profile = request.user 

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(request, 'profiles/edit_profile.html', context)

@login_required
def order_history(request, order_number):
    """ Display details of a past order """
    order = get_object_or_404(Order, order_number=order_number, user_profile=request.user)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, 'profiles/order_history.html', context)





