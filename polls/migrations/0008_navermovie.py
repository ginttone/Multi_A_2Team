# Generated by Django 3.2.3 on 2021-07-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210727_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=5, default=False, max_digits=20)),
                ('author', models.CharField(max_length=90)),
                ('rating', models.DecimalField(decimal_places=5, default=False, max_digits=20)),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('nation', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
            ],
        ),
    ]
