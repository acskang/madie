# Generated by Django 2.1.8 on 2019-05-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_게시판테이블헤드'),
    ]

    operations = [
        migrations.AddField(
            model_name='게시판테이블헤드',
            name='순서',
            field=models.IntegerField(null=True),
        ),
    ]
