# Generated by Django 4.2 on 2023-04-07 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_rename_featured_image_item_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='title',
        ),
    ]