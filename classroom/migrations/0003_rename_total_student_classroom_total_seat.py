# Generated by Django 5.1.3 on 2024-11-25 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_alter_classroom_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='total_student',
            new_name='total_seat',
        ),
    ]