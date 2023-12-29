from rest_framework import viewsets
from meteo.models import *
from meteo.serializers import *

class MeteoViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'head','put','delete']
    serializer_class = MeteoSerializer
    queryset = Meteo.objects.all().order_by('-id')
