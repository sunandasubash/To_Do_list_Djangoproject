# Generated by Django 4.2.3 on 2023-07-25 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_table1_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table1',
            old_name='date',
            new_name='date1',
        ),
    ]
