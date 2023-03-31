# Generated by Django 4.1.7 on 2023-03-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_users_last_name_alter_users_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='house_type',
            field=models.CharField(choices=[('Select your house type', 'Select your house type'), ('Private House', 'Private House'), ('Cottage', 'Cottage')], default='No house type selected', max_length=50, verbose_name='House Type'),
        ),
    ]