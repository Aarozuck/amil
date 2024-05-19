from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_rent/', views.create_rent, name='create_rent'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
   path('like_product/<int:product_id>/', views.like_product, name='like_product'),
   path('rent_details/<int:rent_id>/', views.rent_details, name='rent_details'),
   path('add_rent_comment/<int:rent_id>/', views.add_rent_comment, name='add_rent_comment'),
   path('add_product_comment/<int:product_id>/', views.add_product_comment, name='add_product_comment'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('rent_details/<int:rent_id>/', views.rent_details, name='rent_details'),
    path('search/', views.search, name='search'),
]

