# Generated by Django 4.0.4 on 2022-05-26 19:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('user_management', '0003_user_biography_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='profile_image',
        ),
    ]