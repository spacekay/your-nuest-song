# Generated by Django 3.2.8 on 2021-12-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_case_n_s_para'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='surveyed',
            field=models.IntegerField(default=0),
        ),
    ]
