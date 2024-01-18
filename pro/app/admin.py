from django.contrib import admin

# Register your models here.
from .models import Shoes,CartItem

admin.site.register(Shoes)
admin.site.register(CartItem)