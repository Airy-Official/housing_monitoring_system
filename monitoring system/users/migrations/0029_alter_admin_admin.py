# Generated by Django 4.1.7 on 2023-03-28 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_users_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]