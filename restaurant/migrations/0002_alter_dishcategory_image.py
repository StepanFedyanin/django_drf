# Generated by Django 5.0.1 on 2024-02-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='category'),
        ),
    ]
