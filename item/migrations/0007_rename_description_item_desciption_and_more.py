# Generated by Django 4.2 on 2023-04-07 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_rename_name_item_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='desciption',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
    ]
