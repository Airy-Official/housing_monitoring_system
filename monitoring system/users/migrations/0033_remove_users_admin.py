# Generated by Django 4.1.7 on 2023-03-28 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_users_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='admin',
        ),
    ]
