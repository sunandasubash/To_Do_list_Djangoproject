# Generated by Django 4.2.3 on 2023-07-25 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_date_table1_date1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table1',
            old_name='date1',
            new_name='date',
        ),
    ]
