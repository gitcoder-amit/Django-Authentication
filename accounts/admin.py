from django.contrib import admin
from .models import CustomUser, Order

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Order)
