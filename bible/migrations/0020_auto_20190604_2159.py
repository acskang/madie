# Generated by Django 2.1.8 on 2019-06-04 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0019_auto_20190604_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='성경절텝',
            old_name='문단시작',
            new_name='단락시작',
        ),
    ]
