# Generated by Django 2.1.8 on 2019-06-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='성경책텝',
            name='언어',
            field=models.IntegerField(choices=[(1, '한국어'), (2, '영어')]),
        ),
        migrations.AlterField(
            model_name='성경책텝',
            name='책명',
            field=models.IntegerField(choices=[(1, '개역개정 성경전서'), (2, 'NIV Bible'), (3, 'Good News Bible')]),
        ),
    ]
