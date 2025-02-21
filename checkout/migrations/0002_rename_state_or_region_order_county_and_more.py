# Generated by Django 5.1.5 on 2025-02-20 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='state_or_region',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line2',
            new_name='street_address2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='town_or_city',
        ),
    ]
