# Generated by Django 3.2.20 on 2023-07-21 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_mentee_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]