# Generated by Django 3.2.9 on 2021-11-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='First_Name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Last_Name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Password',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Social',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('youtube', 'Youtube'), ('github', 'Github')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
