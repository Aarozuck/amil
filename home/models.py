# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address_choices = (
        ('Mekelle', 'Mekelle'),
        ('Addis Ababa', 'Addis Ababa'),
        ('Adigrat', 'Adigrat'),
    )
    address = models.CharField(max_length=50, choices=address_choices)
    profile_picture = models.ImageField()
    phone_number = models.CharField(max_length=15)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    price_choices = (
        ('piece', 'Per Piece'),
        ('jmla', 'Per Jmla'),
        ('packet', 'Per Packet'),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=10, choices=price_choices)
    ordering_phone_number = models.CharField(max_length=15)
    likes = models.IntegerField(default=0)


class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_product_choices = (
        ('house', 'House'),
        ('car', 'Car'),
        ('bicycle', 'Bicycle'),
        ('motor', 'Motor'),
    )
    type_of_product = models.CharField(max_length=50, choices=type_of_product_choices)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    price_choices = (
        ('day', 'Per Day'),
        ('hour', 'Per Hour'),
        ('week', 'Per Week'),
        ('year', 'Per Year'),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=10, choices=price_choices)
    ordering_phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class RentComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Subject(models.Model):
    name = models.CharField(max_length=100)

class Tutoring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='tutor_photos')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_choices = (
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per = models.CharField(max_length=10, choices=price_per_choices)
    subjects = models.ManyToManyField(Subject)
    phone_number = models.CharField(max_length=15)

class TutoringComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutoring = models.ForeignKey(Tutoring, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)