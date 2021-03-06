# Generated by Django 2.1.1 on 2018-09-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=None, max_length=200, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=None, max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(default=None, max_length=200, verbose_name='Choice'),
        ),
    ]
