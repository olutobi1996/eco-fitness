# Generated by Django 5.1.7 on 2025-05-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_us", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutus",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
