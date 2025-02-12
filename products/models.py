from django.db import models 
from django.contrib.sites.models import Site
from django.utils.timezone import now

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('fitness_plan', 'Fitness Plan'),
        ('diet_plan', 'Diet Plan'),
    ]
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.friendly_name or self.name

class Product(models.Model):
    PRODUCT_TYPES = [
        ('clothing', 'Clothing'),
        ('fitness_plan', 'Fitness Plan'),
        ('diet_plan', 'Diet Plan'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class DietPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_weeks = models.IntegerField(null=True, blank=True)  # Allow NULL values
    image = models.ImageField(upload_to='dietplan_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class FitnessPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_weeks = models.IntegerField(null=True, blank=True)  
    image = models.ImageField(upload_to='fitnessplan_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Keep only auto_now_add
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

