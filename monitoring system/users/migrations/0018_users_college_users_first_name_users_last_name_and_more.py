# Generated by Django 4.1.7 on 2023-03-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_users_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='college',
            field=models.CharField(choices=[('Select your college/department', 'Select your college/department'), ('COE', 'College of Engineering'), ('CON', 'College of Nursing'), ('CISC', 'College of Information Sciences and Computing'), ('CBM', 'College of Business Management'), ('CAS', 'College of Arts and Sciences'), ('CFES', 'College of Forestry and Environmental Science'), ('COA', 'College of Agriculture'), ('COED', 'College of Education'), ('CVM', 'College of Veterinary Medicine'), ('Other', 'Other Office'), ('Dugangan pa', 'Dugangan pa')], default='No College Selected', max_length=100, verbose_name='College/Department'),
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.TextField(default='no first name specified', max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.TextField(default='no last name specified', max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='no username specified', max_length=25),
        ),
    ]