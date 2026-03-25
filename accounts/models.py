from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # image will be stored in root folder inside profile_images folder
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()


    def __str__(self):
        return self.phone_number
    

# just for querying purpose, not for authentication
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_number} by {self.user.phone_number}"

