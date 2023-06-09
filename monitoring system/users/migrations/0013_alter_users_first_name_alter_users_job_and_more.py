# Generated by Django 4.1.7 on 2023-03-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_users_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.TextField(default='no first name specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='job',
            field=models.TextField(default='no job specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.TextField(default='no last name specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='middle_name',
            field=models.TextField(default='no middle name specified', max_length=50),
        ),
    ]
