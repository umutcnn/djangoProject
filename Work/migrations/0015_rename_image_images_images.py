# Generated by Django 4.1.2 on 2022-12-22 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0014_rename_images_images_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image',
            new_name='images',
        ),
    ]
