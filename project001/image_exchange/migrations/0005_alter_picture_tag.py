# Generated by Django 4.1 on 2023-02-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_exchange', '0004_rename_photo_picture_image_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='tag',
            field=models.CharField(default='null', max_length=2000),
        ),
    ]
