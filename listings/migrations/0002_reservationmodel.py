# Generated by Django 3.2 on 2021-08-03 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_type', to='listings.listing')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_room', to='listings.hotelroomtype')),
            ],
        ),
    ]
