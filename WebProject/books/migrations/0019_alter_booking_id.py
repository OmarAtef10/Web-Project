# Generated by Django 3.2.4 on 2021-07-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_alter_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.CharField(default='<django.db.models.fields.related.ForeignKey><django.db.models.fields.related.ForeignKey>', max_length=100, primary_key=True, serialize=False),
        ),
    ]
