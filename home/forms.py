from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ProductComment, RentComment , UserProfile, Product, Rent


class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    address_choices = (
        ('Mekelle', 'Mekelle'),
        ('Addis Ababa', 'Addis Ababa'),
        ('Adigrat', 'Adigrat'),
    )
    address = forms.ChoiceField(choices=address_choices)
    profile_picture = forms.ImageField()
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username','password1', 'password2', 'full_name', 'address', 'profile_picture', 'phone_number']



class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']

class RentCommentForm(forms.ModelForm):
    class Meta:
        model = RentComment
        fields = ['text']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'address', 'profile_picture', 'phone_number')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image1', 'image2', 'price','price_type', 'ordering_phone_number')

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('type_of_product', 'name', 'description', 'image1','price', 'image2', 'price_type', 'ordering_phone_number')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')