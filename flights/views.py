from datetime import datetime

from rest_framework import generics

from flights import serializers
from flights.models import Booking, Flight

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner, ThreeDaysRule


class FlightsList(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer
    permission_classes = [IsAuthenticated]


class BookingsList(generics.ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = serializers.BookingSerializer


class BookingDetails(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingDetailsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    permission_classes = [IsOwner, IsAdminUser]


class UpdateBooking(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.UpdateBookingSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    permission_classes = [IsOwner, IsAdminUser, ThreeDaysRule]


class CancelBooking(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    permission_classes = [IsOwner, IsAdminUser, ThreeDaysRule]


class BookFlight(generics.CreateAPIView):
    serializer_class = serializers.UpdateBookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, flight_id=self.kwargs["flight_id"])


class CreateBooking(generics.CreateAPIView):
    serializer_class = serializers.UpdateBookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, flight_id=self.kwargs["flight_id"])
