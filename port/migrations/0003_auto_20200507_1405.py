# Generated by Django 3.0.6 on 2020-05-07 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20200507_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['id']},
        ),
    ]