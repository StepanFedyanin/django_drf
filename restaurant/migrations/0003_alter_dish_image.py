# Generated by Django 5.0.1 on 2024-02-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_dishcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(upload_to='dish'),
        ),
    ]
