# Generated by Django 2.1.8 on 2019-06-03 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bible', '0014_auto_20190604_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='성경권텝',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('권명', models.CharField(choices=[('한국어', (('창', '창세기'), ('출', '출애굽기'))), ('English', (('Gen', 'Genesis'), ('Exo', 'Exodus')))], max_length=6)),
                ('구분', models.PositiveIntegerField(choices=[(1, '구약'), (2, '신약'), (3, 'Old Testment'), (4, 'New Testment')])),
                ('순서', models.PositiveIntegerField()),
                ('절수', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='성경문단텝',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('제목', models.CharField(max_length=100)),
                ('권명', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='문단들', to='bible.성경권텝')),
            ],
        ),
        migrations.CreateModel(
            name='성경장텝',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('번호', models.PositiveIntegerField()),
                ('권명', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='장들', to='bible.성경권텝')),
            ],
        ),
        migrations.CreateModel(
            name='성경절텝',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('번호', models.PositiveIntegerField()),
                ('내용', models.TextField()),
                ('문단시작', models.BooleanField(default=False)),
                ('작성일', models.DateTimeField(auto_now_add=True)),
                ('수정일', models.DateTimeField(null=True)),
                ('작성자', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='작성자', to=settings.AUTH_USER_MODEL)),
                ('장번호', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='절들', to='bible.성경장텝')),
            ],
        ),
        migrations.CreateModel(
            name='성경책텝',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('서명', models.PositiveIntegerField(choices=[(1, '개역개정 성경전서'), (2, 'NIV Bible'), (3, 'Good News Bible')])),
                ('언어', models.PositiveIntegerField(choices=[(1, '한국어'), (2, 'English')])),
            ],
        ),
        migrations.AddField(
            model_name='성경권텝',
            name='서명',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='권들', to='bible.성경책텝'),
        ),
    ]