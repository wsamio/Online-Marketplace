# Generated by Django 4.2 on 2023-04-07 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_category_alter_item_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='desciption',
            new_name='description',
        ),
    ]