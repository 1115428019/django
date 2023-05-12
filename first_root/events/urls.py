from django.urls import path, re_path
from . import views

urlpatterns = [
      re_path(r'api/flight/(?P<flightId>\d+)',views.getFlightId,name='getFlightId'),
      path('api/flights',views.getALLFlights,name='getALLFlights'),
      path('api/book',views.postBook,name='postBook'),
      re_path(r'api/booking/(?P<bookingId>\d+)',views.getBookingId,name='getBookingId'),
      path('api/comfirmbooking',views.putConfirmBooking,name='putConfirmBooking'),
      re_path(r'api/cancelbooking/(?P<bookingId>\d+)',views.putCancelBookingId,name='putCancelBookingId'),
      path('api/paymentproviders',views.getPaymentProviders,name='getPaymentProviders'),
      re_path(r'api/payBooking/\d+',views.postPayBookingId,name='postPayBookingId')
]