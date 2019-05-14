# Generated by Django 2.1.3 on 2019-05-14 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weblate_web', '0003_auto_20190509_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('release', 'Release'), ('feature', 'Features'), ('announce', 'Announcement'), ('localization', 'Localization')], db_index=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(blank=True, help_text='Will be generated from first body paragraph if empty'),
        ),
    ]
