# Generated by Django 5.1a1 on 2024-09-28 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_type_id',
            new_name='user_type',
        ),
    ]