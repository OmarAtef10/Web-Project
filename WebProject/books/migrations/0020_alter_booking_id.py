# Generated by Django 3.2.4 on 2021-07-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_alter_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
