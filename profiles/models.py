from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class UserProfile(AbstractUser):
    """Extended user model to store additional profile details"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    street_address1 = models.CharField(max_length=100, blank=True, null=True)
    street_address2 = models.CharField(max_length=100, blank=True, null=True)
    town_or_city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    country = CountryField(blank_label='Country', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    saved_items = models.ManyToManyField('products.Product', blank=True, related_name='saved_by_users')

    def __str__(self):
        return self.username

    def get_full_address(self):
        """Returns full formatted address for the user profile"""
        return f"{self.street_address1}, {self.street_address2 or ''}, {self.town_or_city}, {self.county or ''}, {self.postcode}, {self.country.name if self.country else ''}".strip(', ')

