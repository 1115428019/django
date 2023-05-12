from django.db import models

# Create your models here.
import datetime

class Aircraft(models.Model):
    id = models.AutoField('Aircraft id',primary_key=True)
    tail_number = models.CharField('Aircraft tail number', max_length=120)
    type = models.CharField('Aircraft type', max_length=60)
    number_of_seats = models.PositiveSmallIntegerField('Aircraft number of seats',default=150)




class Airport(models.Model):
    id = models.AutoField('Airport id',primary_key=True)
    name = models.CharField('Airport name', max_length=120)
    country = models.CharField('Airport country', max_length=60)
    time_zone = models.PositiveSmallIntegerField('Airport time zone',default=0)



class Flight(models.Model):
    id = models.AutoField('Flight id',primary_key=True)
    flight_number = models.CharField('Flight number',max_length=60)
    duration = models.DateTimeField('Flight duration')
    departure_datetime = models.DateTimeField('Flight departure datetime' )
    price_per_seat = models.DecimalField('Flight price per seat',max_digits=3,decimal_places=0)
    cost_per_seat =  models.DecimalField('Flight cost per seat',max_digits=3,decimal_places=0)
    aircraft = models.ForeignKey("Aircraft", to_field='id',on_delete=models.DO_NOTHING)
    destination_airport =models.ForeignKey("Airport", to_field='id',related_name='Flight_destination_airport',on_delete=models.DO_NOTHING)
    departure_airport = models.ForeignKey("Airport", to_field='id',related_name='Flight_departure_airport',on_delete=models.DO_NOTHING)





class Customer(models.Model):
    id = models.AutoField('Customer id', primary_key=True)
    first_name = models.CharField('Customer first name',max_length=60)
    last_name = models.CharField('Customer last name',max_length=60)
    passport_number = models.CharField('Customer passport number', max_length=60)
    phone_number = models.TextField('Customer phone number')
    email_address = models.EmailField('Customer email address')
    date_of_birth = models.DateField('Customer date of birth')
    home_address = models.TextField('Customer home address',blank = True,null=True)
    allergies = models.TextField('Customer allergies',blank = True,null=True)




class PSP(models.Model):
    id = models.AutoField('PSP id', primary_key=True)
    name = models.CharField('PSP name', max_length=120)
    url = models.URLField('PSP url',max_length=200)
    account_id = models.PositiveSmallIntegerField('PSP account id',default=0)
    username = models.CharField('PSP username',max_length=60)
    password = models.CharField('PSP password',max_length=60)





class Booking(models.Model):
    id = models.AutoField('Booking id', primary_key=True)
    flight = models.ForeignKey('Flight',to_field='id',related_name='Booking_flight',on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('Customer',to_field='id',related_name='Booking_customer',on_delete=models.DO_NOTHING)
    payment_provider = models.ForeignKey('PSP',to_field='id',related_name='Booking_payment_provider',on_delete=models.DO_NOTHING,blank = True,null=True)
    price = models.DecimalField('Booking price',max_digits=3,decimal_places=2)
    booking_datetime = models.DateTimeField('Booking datetime',auto_now_add=True)
    transaction_id = models.CharField('Booking transaction id',max_length=120)
    success_key = models.CharField('Booking success key',max_length=120)
    booking_status = models.CharField('Booking status',max_length=30,choices=(('Confirmed','Confirmed'),('fail','fail'),('on_hold','on_hold')),default='on_hold')





class Ticket(models.Model):
    id = models.AutoField('Ticket id', primary_key=True)
    booking = models.ForeignKey('Booking',to_field='id',related_name='Ticket_booking',on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('Customer',to_field='id',related_name='Ticket_customer',on_delete=models.DO_NOTHING)
    seat_number = models.CharField('Ticket seat number', max_length=120)


