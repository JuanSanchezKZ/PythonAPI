# Generated by Django 2.2 on 2022-10-09 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='title',
            new_name='status_text',
        ),
    ]
