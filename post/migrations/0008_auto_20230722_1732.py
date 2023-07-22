# Generated by Django 3.2.20 on 2023-07-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='destination_country_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='source_country_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]