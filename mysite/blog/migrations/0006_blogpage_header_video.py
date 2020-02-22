# Generated by Django 2.2.9 on 2020-02-22 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailvideos', '0010_video_ordering'),
        ('blog', '0005_blogtagindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='header_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailvideos.Video'),
        ),
    ]
