# Generated by Django 4.1.2 on 2022-12-22 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0013_rename_image_tag_images_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
    ]
