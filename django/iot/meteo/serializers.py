from rest_framework import serializers
from meteo.models import *

class MeteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meteo
        fields = "__all__"