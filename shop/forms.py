# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser, Review,Product

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2', 'role']

# from .models import Product

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price', 'stock', 'category', 'image', 'tags']

# from .models import Review

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'comment']  

# shop/forms.py
# shop/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product, Review

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'image', 'tags']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']