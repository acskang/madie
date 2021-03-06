# Generated by Django 2.1.8 on 2019-05-30 08:35

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='thumb',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.Album'),
        ),
    ]
