# Generated by Django 3.2.20 on 2023-07-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
