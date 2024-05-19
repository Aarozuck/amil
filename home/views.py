from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ProductCommentForm, RentCommentForm, RentForm, UserRegistrationForm,ProductForm
from .models import Product, Rent, UserProfile
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            full_name = form.cleaned_data['full_name']
            address = form.cleaned_data['address']
            profile_picture = form.cleaned_data['profile_picture']
            phone_number = form.cleaned_data['phone_number']
            UserProfile.objects.create(user=user, full_name=full_name, address=address, profile_picture=profile_picture, phone_number=phone_number)
            login(request, user)
            return redirect('profile', user_id=user.id)
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    products = Product.objects.all()
    rent = Rent.objects.all()
    content = {
        'products': products,
        'rent' : rent
    }
    return render(request, 'home.html',content )

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})




@login_required
def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
    return redirect('home')


@login_required
def create_rent(request):
    if request.method == 'POST':
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.user = request.user
            rent.save()
            return redirect('home')
    else:
        form = RentForm()
    return render(request, 'create_rent.html', {'form': form})

@login_required
def profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    return render(request, 'profile.html', {'user_profile': user_profile})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_details', product_id=product.id)
    else:
        form = ProductCommentForm()
    return render(request, 'product_details.html', {'product': product, 'form': form})


def rent_details(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    if request.method == 'POST':
        form = RentCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rent = rent
            comment.user = request.user
            comment.save()
            return redirect('rent_details', rent_id=rent.id)
    else:
        form = RentCommentForm()
    return render(request, 'rent_details.html', {'rent': rent, 'form': form})



def add_product_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_details', product_id=product.id)
    else:
        form = ProductCommentForm()
    return render(request, 'add_product_comment.html', {'form': form})

def add_rent_comment(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    if request.method == 'POST':
        form = RentCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rent = rent
            comment.user = request.user
            comment.save()
            return redirect('rent_details', rent_id=rent.id)
    else:
        form = RentCommentForm()
    return render(request, 'add_rent_comment.html', {'form': form})



from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    rents = Rent.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products,
        'rents': rents,
    }
    return render(request, 'search_results.html', context)
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})

def rent_details(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    return render(request, 'rent_details.html', {'rent': rent})

