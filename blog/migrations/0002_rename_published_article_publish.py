# Generated by Django 3.2.9 on 2021-11-30 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='publish',
        ),
    ]
