# Generated by Django 3.2.3 on 2021-07-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_nmovie_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.DecimalField(decimal_places=5, default=0, max_digits=20)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='nmovie',
            name='score',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
    ]
