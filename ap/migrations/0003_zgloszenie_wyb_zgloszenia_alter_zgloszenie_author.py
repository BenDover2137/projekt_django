# Generated by Django 5.1.2 on 2024-12-06 05:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0002_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='zgloszenie',
            name='wyb_zgloszenia',
            field=models.ForeignKey(limit_choices_to={'profile__role': 'tech'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wyb_zgl', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zgloszenie',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL),
        ),
    ]
