# Generated by Django 5.0.2 on 2024-03-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
