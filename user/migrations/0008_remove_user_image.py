# Generated by Django 5.1.3 on 2024-11-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
