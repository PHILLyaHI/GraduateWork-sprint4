# Generated by Django 4.0.3 on 2022-09-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0009_remove_profile_is_banned_comment_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]