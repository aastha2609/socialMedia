# Generated by Django 3.1 on 2021-07-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0031_remove_comment_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.TextField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
