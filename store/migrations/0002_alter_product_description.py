# Generated by Django 5.0.2 on 2024-02-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, unique=True),
        ),
    ]
