# Generated by Django 2.1.4 on 2019-01-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answering_end', models.DateTimeField(verbose_name='date published')),
                ('display_end', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=200)),
                ('choice_1', models.TextField(max_length=200)),
                ('choice_2', models.TextField(max_length=200)),
                ('choice_3', models.TextField(max_length=200)),
                ('choice_4', models.TextField(max_length=200)),
                ('correct_choice', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.AddField(
            model_name='currentquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.Question'),
        ),
    ]
