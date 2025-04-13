# from django.shortcuts import render, redirect
# from .forms import RegisterForm, ReviewForm,Product,ProductForm
# from .models import CartItem, Order, CustomUser, OrderItem, Cart,Category, Review
# from django.contrib.auth import login

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = RegisterForm()
#     return render(request, 'shop/register.html', {'form': form})

# from django.contrib.auth.views import LoginView, LogoutView

# class CustomLoginView(LoginView):
#     template_name = 'shop/login.html'
#     redirect_authenticated_user = True

# class CustomLogoutView(LogoutView):
#     next_page = 'home'

# from django.contrib.auth.decorators import login_required
# from .models import Wishlist

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user = request.user
#         user.first_name = request.POST['first_name']
#         user.last_name = request.POST['last_name']
#         user.email = request.POST['email']
#         user.phone = request.POST['phone']
#         user.address = request.POST['address']
#         user.save()
#         return redirect('profile')
#     wishlist = Wishlist.objects.filter(user=request.user)
#     orders = Order.objects.filter(user=request.user)
#     return render(request, 'shop/profile.html', {'wishlist': wishlist, 'orders': orders})

# @login_required
# def add_to_wishlist(request, product_id):
#     product = Product.objects.get(id=product_id)
#     Wishlist.objects.get_or_create(user=request.user, product=product)
#     return redirect('profile')

# @login_required
# def remove_from_wishlist(request, wishlist_id):
#     Wishlist.objects.get(id=wishlist_id, user=request.user).delete()
#     return redirect('profile')

# from .models import Product, Category
# from .forms import ProductForm
# from django.contrib.auth.decorators import user_passes_test

# def seller_required(user):
#     return user.is_authenticated and user.role == 'seller'

# @user_passes_test(seller_required)
# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.seller = request.user
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'shop/product_form.html', {'form': form})

# @user_passes_test(seller_required)
# def product_update(request, product_id):
#     product = Product.objects.get(id=product_id, seller=request.user)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'shop/product_form.html', {'form': form})

# @user_passes_test(seller_required)
# def product_delete(request, product_id):
#     product = Product.objects.get(id=product_id, seller=request.user)
#     product.delete()
#     return redirect('product_list')

# from django.db.models import Q

# def product_list(request):
#     products = Product.objects.all()
#     query = request.GET.get('q')
#     category = request.GET.get('category')
#     sort = request.GET.get('sort')

#     if query:
#         products = products.filter(Q(name__icasecontains=query) | Q(description__icasecontains=query))
#     if category:
#         products = products.filter(category__slug=category)
#     if sort == 'price_asc':
#         products = products.order_by('price')
#     elif sort == 'price_desc':
#         products = products.order_by('-price')
#     elif sort == 'popularity':
#         products = products.order_by('-id')  # Placeholder

#     categories = Category.objects.all()
#     return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})


# def product_detail(request, product_id):
#     product = Product.objects.get(id=product_id)
#     reviews = Review.objects.filter(product=product)
#     return render(request, 'shop/product_detail.html', {'product': product, 'reviews': reviews})

# @login_required
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not item_created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('cart')

# @login_required
# def cart(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)
#     total = sum(item.subtotal() for item in cart_items)
#     return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

# @login_required
# def update_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
#     quantity = int(request.POST.get('quantity', 1))
#     if quantity > 0:
#         cart_item.quantity = quantity
#         cart_item.save()
#     else:
#         cart_item.delete()
#     return redirect('cart')

# @login_required
# def remove_from_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
#     cart_item.delete()
#     return redirect('cart')

# @login_required
# def checkout(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)
#     total = sum(item.subtotal() for item in cart_items)

#     if request.method == 'POST':
#         order = Order.objects.create(
#             user=request.user,
#             total_price=total,
#             address=request.POST['address'],
#             payment_method=request.POST['payment_method']
#         )
#         for item in cart_items:
#             OrderItem.objects.create(
#                 order=order,
#                 product=item.product,
#                 quantity=item.quantity,
#                 price=item.product.price
#             )
#             item.product.stock -= item.quantity
#             item.product.save()
#         cart_items.delete()
#         return redirect('order_confirmation', order.id)
#     return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total': total})

# def order_confirmation(request, order_id):
#     order = Order.objects.get(id=order_id, user=request.user)
#     return render(request, 'shop/order_confirmation.html', {'order': order})

# from django.contrib.auth.decorators import user_passes_test
# from django.db.models import Sum

# def admin_required(user):
#     return user.is_authenticated and user.role == 'admin'

# @user_passes_test(admin_required)
# def admin_dashboard(request):
#     users = CustomUser.objects.all()
#     products = Product.objects.all()
#     orders = Order.objects.all()
#     total_sales = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
#     return render(request, 'shop/admin_dashboard.html', {
#         'users': users,
#         'products': products,
#         'orders': orders,
#         'total_sales': total_sales
#     })

# @user_passes_test(admin_required)
# def deactivate_user(request, user_id):
#     user = CustomUser.objects.get(id=user_id)
#     user.is_active = False
#     user.save()
#     return redirect('admin_dashboard')

# @login_required
# def add_review(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.product = product
#             review.save()
#             return redirect('product_detail', product_id)
#     else:
#         form = ReviewForm()
#     return render(request, 'shop/review_form.html', {'form': form, 'product': product})
# shop/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .forms import RegisterForm, ProductForm
from .models import CustomUser, Product, Category, Wishlist, Cart, CartItem, Order, OrderItem

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'shop/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'home'

def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.address = request.POST['address']
        user.save()
        return redirect('profile')
    wishlist = Wishlist.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/profile.html', {'wishlist': wishlist, 'orders': orders})


def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('profile')

def remove_from_wishlist(request, wishlist_id):
    Wishlist.objects.get(id=wishlist_id, user=request.user).delete()
    return redirect('profile')

def seller_required(user):
    return user.is_authenticated and user.role == 'seller'


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})


def product_update(request, product_id):
    product = Product.objects.get(id=product_id, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form})


def product_delete(request, product_id):
    product = Product.objects.get(id=product_id, seller=request.user)
    product.delete()
    return redirect('product_list')

def product_list(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    if query:
        products = products.filter(Q(name__icasecontains=query) | Q(description__icasecontains=query))
    if category:
        products = products.filter(category__slug=category)
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'popularity':
        products = products.order_by('-id')

    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


def update_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')


def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.subtotal() for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total,
            address=request.POST['address'],
            payment_method=request.POST['payment_method']
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            item.product.stock -= item.quantity
            item.product.save()
        cart_items.delete()
        return redirect('order_confirmation', order.id)
    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total': total})

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'shop/order_confirmation.html', {'order': order})

# shop/views.py (add at the end)
from .forms import ReviewForm
from .models import Review

def add_review(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id)
    else:
        form = ReviewForm()
    return render(request, 'shop/review_form.html', {'form': form, 'product': product})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'shop/product_detail.html', {'product': product, 'reviews': reviews})