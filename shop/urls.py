# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     path('logout/', views.CustomLogoutView.as_view(), name='logout'),
# ]

# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# urlpatterns += [
#     path('password_reset/', PasswordResetView.as_view(template_name='shop/password_reset.html'), name='password_reset'),
#     path('password_reset/done/', PasswordResetDoneView.as_view(template_name='shop/password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('reset/done/', PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'), name='password_reset_complete'),
# ]

# urlpatterns += [
#     path('profile/', views.profile, name='profile'),
#     path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_wishlist'),
#     path('wishlist/remove/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_wishlist'),
# ]

# urlpatterns += [
#     path('', views.product_list, name='home'),
#     path('products/', views.product_list, name='product_list'),
#     path('product/add/', views.product_create, name='product_create'),
#     path('product/edit/<int:product_id>/', views.product_update, name='product_update'),
#     path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),
# ]

# urlpatterns += [
#     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
# ]

# urlpatterns += [
#     path('cart/', views.cart, name='cart'),
#     path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
# ]

# urlpatterns += [
#     path('checkout/', views.checkout, name='checkout'),
#     path('order/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
# ]

# urlpatterns += [
#     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
#     path('user/deactivate/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
# ]

# urlpatterns += [
#     path('product/<int:product_id>/review/', views.add_review, name='add_review'),
# ]

# shop/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.product_list, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_wishlist'),
    path('wishlist/remove/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_wishlist'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/add/', views.product_create, name='product_create'),
    path('product/edit/<int:product_id>/', views.product_update, name='product_update'),
    path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('password_reset/', PasswordResetView.as_view(template_name='shop/password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='shop/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'), name='password_reset_complete'),
]

# shop/urls.py
urlpatterns += [
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
]