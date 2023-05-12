# Generated by Django 3.2.17 on 2023-05-11 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20230207_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Aircraft id')),
                ('tail_number', models.CharField(max_length=120, verbose_name='Aircraft tail number')),
                ('type', models.CharField(max_length=60, verbose_name='Aircraft type')),
                ('number_of_seats', models.PositiveSmallIntegerField(default=150, verbose_name='Aircraft number of seats')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Airport id')),
                ('name', models.CharField(max_length=120, verbose_name='Airport name')),
                ('country', models.CharField(max_length=60, verbose_name='Airport country')),
                ('time_zone', models.PositiveSmallIntegerField(default=0, verbose_name='Airport time zone')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Booking id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Booking price')),
                ('booking_datetime', models.DateTimeField(verbose_name='Booking datetime')),
                ('transaction_id', models.CharField(max_length=120, verbose_name='Booking transaction id')),
                ('success_key', models.CharField(max_length=120, verbose_name='Booking success key')),
                ('booking_status', models.CharField(choices=[('success', 'success'), ('fail', 'fail')], default='success', max_length=30, verbose_name='Booking status')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Customer id')),
                ('first_name', models.CharField(max_length=60, verbose_name='Customer first name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Customer last name')),
                ('passport_number', models.CharField(max_length=60, verbose_name='Customer passport number')),
                ('phone_number', models.TextField(verbose_name='Customer phone number')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Customer email address')),
                ('date_of_birth', models.DateField(verbose_name='Customer date of birth')),
                ('home_address', models.TextField(verbose_name='Customer home address')),
                ('allergies', models.TextField(verbose_name='Customer allergies')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Flight id')),
                ('flight_number', models.CharField(max_length=60, verbose_name='Flight number')),
                ('duration', models.DateTimeField(verbose_name='Flight duration')),
                ('departure_datetime', models.DateTimeField(verbose_name='Flight departure datetime')),
                ('price_per_seat', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Flight price per seat')),
                ('cost_per_seat', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Flight cost per seat')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.aircraft')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Flight_departure_airport', to='events.airport')),
                ('destination_airport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Flight_destination_airport', to='events.airport')),
            ],
        ),
        migrations.CreateModel(
            name='PSP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='PSP id')),
                ('name', models.CharField(max_length=120, verbose_name='PSP name')),
                ('url', models.URLField(verbose_name='PSP url')),
                ('account_id', models.PositiveSmallIntegerField(default=0, verbose_name='PSP account id')),
                ('username', models.CharField(max_length=60, verbose_name='PSP username')),
                ('password', models.CharField(max_length=60, verbose_name='PSP password')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Ticket id')),
                ('seat_number', models.CharField(max_length=120, verbose_name='Ticket seat number')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Ticket_booking', to='events.booking')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Ticket_customer', to='events.customer')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='MyClubUser',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Booking_customer', to='events.customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Booking_flight', to='events.flight'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Booking_payment_provider', to='events.psp'),
        ),
    ]