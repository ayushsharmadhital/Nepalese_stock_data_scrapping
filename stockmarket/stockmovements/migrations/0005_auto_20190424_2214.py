# Generated by Django 2.2 on 2019-04-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmovements', '0004_auto_20190424_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhead',
            name='SNo',
            field=models.IntegerField(default=1),
        ),
    ]