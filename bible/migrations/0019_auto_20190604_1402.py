# Generated by Django 2.1.8 on 2019-06-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0018_성경글텝'),
    ]

    operations = [
        migrations.AlterField(
            model_name='성경절텝',
            name='수정일',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]