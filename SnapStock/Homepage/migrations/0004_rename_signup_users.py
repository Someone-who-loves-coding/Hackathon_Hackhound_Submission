# Generated by Django 5.0.2 on 2024-02-16 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_rename_expiry_date_ingredients_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signup',
            new_name='Users',
        ),
    ]
