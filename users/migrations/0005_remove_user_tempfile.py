# Generated by Django 2.2.5 on 2021-01-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_tempfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tempFile',
        ),
    ]
