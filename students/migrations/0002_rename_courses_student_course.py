# Generated by Django 5.1.4 on 2024-12-29 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='courses',
            new_name='course',
        ),
    ]