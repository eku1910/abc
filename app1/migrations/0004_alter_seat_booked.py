# Generated by Django 4.0.2 on 2022-03-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_seat_booked_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='booked',
            field=models.CharField(choices=[('Available', 'Available'), ('Not_Available', 'Not_Available')], default='Available', max_length=20),
        ),
    ]
