# Generated by Django 4.0.6 on 2022-08-09 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shinydb', '0003_shiny_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiny',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
