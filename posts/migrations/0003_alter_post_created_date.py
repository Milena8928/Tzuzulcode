# Generated by Django 4.0.1 on 2022-05-18 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
