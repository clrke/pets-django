from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from listings.models import Pet
from listings.serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
