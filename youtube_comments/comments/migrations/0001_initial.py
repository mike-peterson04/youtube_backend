# Generated by Django 3.1.8 on 2021-05-25 18:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=250)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('parent', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
            ],
        ),
    ]