# Generated by Django 5.1.7 on 2025-03-29 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="user_profile",
            new_name="user",
        ),
    ]
