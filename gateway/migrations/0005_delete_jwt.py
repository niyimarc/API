# Generated by Django 4.1.2 on 2022-12-05 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0004_alter_jwt_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Jwt',
        ),
    ]