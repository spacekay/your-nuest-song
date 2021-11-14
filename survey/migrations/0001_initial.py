# Generated by Django 3.2.8 on 2021-11-15 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_title', models.CharField(max_length=200)),
                ('result_content', models.TextField(max_length=3000, verbose_name='Description')),
                ('result_like', models.IntegerField(default=0)),
                ('result_dislike', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_title', models.CharField(max_length=100)),
                ('song_link', models.CharField(max_length=200)),
                ('song_like', models.IntegerField(default=0)),
                ('song_dislike', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ResultSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=1)),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.result')),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.song')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.CharField(max_length=50)),
                ('choice_text', models.CharField(max_length=200)),
                ('e_i_para', models.IntegerField(default=0)),
                ('n_s_para', models.IntegerField(default=0)),
                ('f_t_para', models.IntegerField(default=0)),
                ('p_j_para', models.IntegerField(default=0)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question')),
            ],
        ),
    ]
