from django.conf import settings
from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("fitness_plans", "Fitness Plans"),
        ("diet_plans", "Diet Plans"),
        ("eco_friendly_activewear", "Eco-Friendly Activewear"),
        ("recycled_fitness_gear", "Recycled Fitness Gear"),
        ("vegan_supplements", "Vegan Supplements"),
        ("biodegradable_accessories", "Biodegradable Accessories"),
    ]
    name = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.friendly_name or self.name

    def get_friendly_name(self):
        return self.friendly_name or dict(self.CATEGORY_CHOICES).get(
            self.name, self.name
        )


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    has_sizes = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


class Bundle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
