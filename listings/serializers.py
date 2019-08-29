from rest_framework import routers, serializers, viewsets

from listings.models import Pet


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ['pk', 'name', 'species', 'breed', 'created_at']
