# Generated by Django 5.1.4 on 2025-01-10 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='text',
            new_name='texts',
        ),
    ]
