from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from listings.views import PetViewSet

router = routers.DefaultRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
