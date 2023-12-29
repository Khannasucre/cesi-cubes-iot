from django.urls import include, path
from rest_framework import routers

import meteo.views as views

router = routers.DefaultRouter()
router.register(r'meteo', views.MeteoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls