# Generated by Django 3.2 on 2022-01-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
