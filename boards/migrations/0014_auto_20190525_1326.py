# Generated by Django 2.1.8 on 2019-05-25 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20190525_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='글텝',
            old_name='수정일',
            new_name='댓글일',
        ),
        migrations.RenameField(
            model_name='글텝',
            old_name='수정자',
            new_name='댓글자',
        ),
    ]
