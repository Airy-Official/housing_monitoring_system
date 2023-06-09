# Generated by Django 4.1.7 on 2023-03-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_users_college_alter_users_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=50, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='users',
            name='job',
            field=models.CharField(max_length=50, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='middle_name',
            field=models.CharField(max_length=20, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=16, verbose_name='Username'),
        ),
    ]
