# Generated by Django 3.2.20 on 2023-07-21 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='user_id',
        ),
    ]
