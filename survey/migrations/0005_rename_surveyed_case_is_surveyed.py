# Generated by Django 3.2.8 on 2021-12-02 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_case_surveyed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='surveyed',
            new_name='is_surveyed',
        ),
    ]
