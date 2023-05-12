from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from events import models
#from django.core import serializers
import json
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
import random

def getFlightId(request,flightId):
     flight = models.Flight.objects.filter(id=flightId)
     final = ""
     if flight.exists():
          final = serializers.serialize('json', queryset=flight)
          return Response(final,status=status.HTTP_200_SUCCESS)
     else:
          return Response(None,status=status.HTTP_404_NOT_FOUND)

def getALLFlights(request):
     departure_datetime = request.json.get('departure_datetime')
     departure_airport = request.json.get('departure_airport')
     destination_airport = request.json.get('destination_airport')
     ticket_number = request.json.get('ticket_number')
     flights = models.Flight.objects.filter(departure_datetime=departure_datetime,departure_airport=departure_airport,destination_airport=destination_airport,)
     final = serializers.serialize('json', queryset=flights)
     return Response(final, status=status.HTTP_200_SUCCESS)

def postPayBookingId(request,bookingId):
     booking = models.Booking.objects.filter(id=bookingId)
     final = ""
     if booking.exists():
          final = serializers.serialize('json',queryset=booking)
          return Response(final, status=status.HTTP_200_SUCCESS)
     else:
          return Response(final,status=status.HTTP_404_NOT_FOUND)

def postBook(request):
     flight_id = request.json.get('flight_id')
     passageListAll = request.json.get('customers')
     for passage_list in passageListAll:
          customer = models.Customer.objects.filter(first_name=passage_list[first_name],last_name=passage_list[last_name],email_address=passage_list[email],
                                               passport_number=passage_list[passport_number],phone_number=passage_list[phone])
          flight = models.Flight.objects.filter(id=flight_id)
          aircraft = flight.aircraft
          one = random.randint(1, 200000)
          two = random.randint(200000, 400000)
          models.Booking.objects.create(flight=flight_id,customer=customer.id,price=flight.price_per_seat,booking_status="on_hold",transaction_id=one,success_key=two)
          total = models.Booking.objects.all().count()
          models.Ticket.objects.create(booking_id=total+1,customer_id=customer.id,seat_number=seat_number)
          json_data = {
               "booking_id":total+1
          }
     return Response(json_data,status=status.HTTP_200_SUCCESS)

def getBookingId(request,bookingId):
     if request.method == "GET":
          bookingDetail = models.Booking.objects.filter(id=bookingId)
          final = ""
          if bookingDetail.exists():
               final = serializers.serialize('json', queryset=bookingDetail)
          else:
               final = "404(the booking is not found)"
          return HttpResponse(final)
     if request.method == "PUT":
          booking = models.Booking.objects.filter(id=bookingId)
          customer = booking.customer
          departure_datetime = request.json.get('departure_datetime')
          passageListAll = request.json.get('customers')
          for passage_list in passageListAll:
               models.Customer.objects.filter(id=customer.id).update(first_name=passage_list[first_name],last_name=passage_list[last_name],email_address=passage_list[email],
                                                                  phone_number=passage_list[phone],passport_number=passage_list[passport_number])
               models.Customer.objects.filter(id=customer.id).update(date_of_birth = passge_list[date_of_birth],home_address=passage_list[home_address],allergies=passage_list[Allergies])
          return Response(None,status=status.HTTP_200_SUCCESS)

def putConfirmBooking(request):
     booking_id = request.json.get('booking_id')
     success_key = request.json.get('success_key')
     booking = models.Booking.objects.filter(id=booking_id)
     if booking.exists():
          if success_key != booking.success_key:
               return Response(None,status=status.HTTP_503_Service_Unavailable)
          models.Booking.objects.filter(id=booking_id).update(booking_status="Confirmed")
          total = models.Booking.objects.all().count()
          customer = booking.customer
          flight = booking.flight
          aircraft = flight.aircraft
          while True:
               test = 1
               seat_number = random.randint(1, aircraft.number_of_seats)
               BookingAll = models.Flight.objects.get(flight=flight.id).Booking_set.all()
               for i in BookingAll:
                    real_seat_number = models.Ticket.objects.filter(booking_id=i.id)
                    if real_seat_number.exists():
                         test = 0
               if test == 1:
                    break
          ticket = models.Ticket.objects.create(booking_id=total + 1, customer_id=customer.id, seat_number=seat_number)
          json_data = {
               "booking_id": total + 1,
               "booking_status": "Confirmed",
               "id":ticket.id,
               "seat_number":seat_number,
               "customer_id":customer.id
          }
          return Response(json_data,status=status.HTTP_200_SUCCESS)
     else:
          return Response(None,status=status.HTTP_404_NOT_FOUND)


def putCancelBookingId(request,bookingId):
     booking = models.Booking.objects.filter(id=bookingId)
     final = ""
     if booking.exists():
          final = serializers.serialize('json', queryset=booking)
          booking.delete()
          return Response(None, status=status.HTTP_200_SUCCESS)
     else:
          final = "404(the booking is not found)"
          return Response(None,status=status.HTTP_404_NOT_FOUND)

def getPaymentProviders(request):
     paymentProviders = models.PSP.objects.filter(id__in=[1,2,3,4])
     final = serializers.serialize('json', queryset=paymentProviders)
     return Response(final,status=status.HTTP_200_SUCCESS)

