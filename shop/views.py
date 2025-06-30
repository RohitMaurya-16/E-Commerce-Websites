from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.urls import reverse
from .forms import UserRegisterForm

# Create your views here.

# Product listing

def product_list(request):
    category = request.GET.get('category')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    categories = Product.CATEGORY_CHOICES
    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories, 'selected_category': category})

# Product detail

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# Cart view

def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': product.price * quantity})
        total += product.price * quantity
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

# Add to cart

def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    product_id = str(pk)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

# Remove from cart

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    product_id = str(pk)
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
    return redirect('cart')

# Checkout
@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')
    order = Order.objects.create(user=request.user)
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(order=order, product=product, quantity=quantity)
    request.session['cart'] = {}
    return render(request, 'shop/checkout.html', {'order': order})

# Registration

@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {'form': form})

@ensure_csrf_cookie
def custom_login(request):
    # This view is only needed if you want to customize the login template
    # Otherwise, you can use Django's built-in login view
    return render(request, 'shop/login.html')

@login_required
def profile_redirect(request):
    return redirect('shop:profile_info')

@login_required
def profile_info(request):
    return render(request, 'shop/profile/info.html')

@login_required
def profile_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/profile/orders.html', {'orders': orders})

@login_required
def profile_payments(request):
    return render(request, 'shop/profile/payments.html')

@login_required
def profile_addresses(request):
    return render(request, 'shop/profile/addresses.html')

@login_required
def profile_wishlist(request):
    return render(request, 'shop/profile/wishlist.html')

@login_required
def profile_security(request):
    return render(request, 'shop/profile/security.html')

@login_required
def profile_preferences(request):
    return render(request, 'shop/profile/preferences.html')
