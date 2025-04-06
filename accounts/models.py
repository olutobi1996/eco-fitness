from django.db import models
from django.contrib.auth.models import User  

class AccountProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username  

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"


