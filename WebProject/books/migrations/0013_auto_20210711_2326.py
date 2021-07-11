# Generated by Django 3.2.4 on 2021-07-11 21:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0012_alter_booking_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('bookedBy', 'bookedBook')},
        ),
    ]
