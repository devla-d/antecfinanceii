# Generated by Django 3.2.9 on 2021-12-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='amount',
            new_name='ref_percent',
        ),
    ]
