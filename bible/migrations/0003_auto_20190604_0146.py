# Generated by Django 2.1.8 on 2019-06-03 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0002_auto_20190604_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='성경책텝',
            old_name='책명',
            new_name='명',
        ),
    ]
