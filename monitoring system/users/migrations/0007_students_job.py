# Generated by Django 4.1.7 on 2023-03-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='job',
            field=models.TextField(default='no job specified'),
        ),
    ]
