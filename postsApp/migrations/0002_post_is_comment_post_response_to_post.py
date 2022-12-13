# Generated by Django 4.1.4 on 2022-12-12 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='response_to_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postsApp.post'),
        ),
    ]