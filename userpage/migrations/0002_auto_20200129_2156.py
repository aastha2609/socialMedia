# Generated by Django 3.0 on 2020-01-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_image'),
        ),
    ]