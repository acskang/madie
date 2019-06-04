# Generated by Django 2.1.8 on 2019-06-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0005_auto_20190604_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='성경권텝',
            name='구분',
            field=models.PositiveIntegerField(choices=[(1, '구약'), (2, '신약'), (3, 'Old Testment'), (4, 'New Testment')]),
        ),
        migrations.AlterField(
            model_name='성경권텝',
            name='권명',
            field=models.CharField(choices=[('한국어', (('창', '창세기'), ('출', '출애굽기'))), ('English', (('Gen', 'Genesis'), ('Exo', 'Exodus')))], max_length=6),
        ),
        migrations.AlterField(
            model_name='성경권텝',
            name='순서',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='성경권텝',
            name='절수',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='성경장텝',
            name='번호',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='성경절텝',
            name='번호',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='성경책텝',
            name='서명',
            field=models.PositiveIntegerField(choices=[(1, '개역개정 성경전서'), (2, 'NIV Bible'), (3, 'Good News Bible')]),
        ),
        migrations.AlterField(
            model_name='성경책텝',
            name='언어',
            field=models.PositiveIntegerField(choices=[(1, '한국어'), (2, 'English')]),
        ),
    ]