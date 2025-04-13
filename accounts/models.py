from django.db import models
from django.contrib.auth.models import User  
from django_countries.fields import CountryField

class AccountProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    default_phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Fields used during checkout
    default_country = CountryField(blank_label='(select country)', blank=True, null=True)
    default_postcode = models.CharField(max_length=20, blank=True, null=True)
    default_town_or_city = models.CharField(max_length=40, blank=True, null=True)
    default_street_address1 = models.CharField(max_length=80, blank=True, null=True)
    default_street_address2 = models.CharField(max_length=80, blank=True, null=True)
    default_county = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.user.username






