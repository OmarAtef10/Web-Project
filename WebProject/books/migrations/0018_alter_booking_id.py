# Generated by Django 3.2.4 on 2021-07-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20210711_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
