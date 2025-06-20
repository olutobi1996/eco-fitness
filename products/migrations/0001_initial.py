# Generated by Django 5.1.7 on 2025-03-29 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bundle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="bundles/")),
                (
                    "original_price",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "discounted_price",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("fitness_plans", "Fitness Plans"),
                            ("diet_plans", "Diet Plans"),
                            (
                                "eco_friendly_activewear",
                                "Eco-Friendly Activewear",
                            ),
                            ("recycled_fitness_gear", "Recycled Fitness Gear"),
                            ("vegan_supplements", "Vegan Supplements"),
                            (
                                "biodegradable_accessories",
                                "Biodegradable Accessories",
                            ),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "friendly_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(blank=True, max_length=50,
                                     null=True, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "rating",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=3, null=True
                    ),
                ),
                (
                    "image_url",
                    models.URLField(blank=True, max_length=1024, null=True),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True,
                                      upload_to="products/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_featured", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.PositiveIntegerField(default=5)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
