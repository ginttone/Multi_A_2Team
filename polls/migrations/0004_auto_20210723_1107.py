# Generated by Django 3.2.3 on 2021-07-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210723_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nmovie',
            old_name='score',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='nmovie',
            old_name='outline',
            new_name='genre',
        ),
        migrations.AddField(
            model_name='nmovie',
            name='nation',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
