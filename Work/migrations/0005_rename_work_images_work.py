# Generated by Django 4.1.2 on 2022-12-15 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0004_alter_work_image_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='work',
            new_name='Work',
        ),
    ]
