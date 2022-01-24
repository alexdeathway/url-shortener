# Generated by Django 4.0.1 on 2022-01-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_model',
            name='id',
        ),
        migrations.AlterField(
            model_name='url_model',
            name='short_url',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]