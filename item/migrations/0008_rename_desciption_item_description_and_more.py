# Generated by Django 4.2 on 2023-04-07 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_rename_description_item_desciption_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='desciption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='title',
        ),
    ]