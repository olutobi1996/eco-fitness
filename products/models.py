from django.db import models 

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('fitness_plans', 'Fitness Plans'),
        ('diet_plans', 'Diet Plans'),
        ('eco_friendly_activewear', 'Eco-Friendly Activewear'),
        ('recycled_fitness_gear', 'Recycled Fitness Gear'),
        ('vegan_supplements', 'Vegan Supplements'),
        ('biodegradable_accessories', 'Biodegradable Accessories'),
    ]
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.friendly_name or self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


