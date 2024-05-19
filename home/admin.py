from django.contrib import admin
from .models import Product,ProductComment,Rent,RentComment, UserProfile

admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(Rent)
admin.site.register(RentComment)
admin.site.register(UserProfile)