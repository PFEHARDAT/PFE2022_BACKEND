# Generated by Django 4.1.4 on 2022-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usersApp", "0002_remove_user_about_remove_user_followers_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="about",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="user",
            name="followers_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="following_count",
            field=models.IntegerField(default=0),
        ),
    ]
