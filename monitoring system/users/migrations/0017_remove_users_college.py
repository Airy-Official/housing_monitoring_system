# Generated by Django 4.1.7 on 2023-03-26 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_users_first_name_remove_users_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='college',
        ),
    ]