from django.urls import include, path
from rest_framework import routers

from apps.studios.views import StudioViewSet

router = routers.DefaultRouter()
router.register(r"studio", StudioViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
