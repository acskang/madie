# Generated by Django 2.1.8 on 2019-06-03 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0006_auto_20190604_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='성경절텝',
            name='징',
        ),
        migrations.DeleteModel(
            name='성경절텝',
        ),
    ]
