from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegistrationSerializer

# Create your views here.
class RegistrationCreateView(CreateAPIView):
    serializer_class = RegistrationSerializer