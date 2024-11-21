from rest_framework import viewsets

from apps.studios.serializers import StudioSerializer
from apps.studios.services import get_studios


class StudioViewSet(viewsets.ViewSet):
    serializer_class = StudioSerializer
    queryset = get_studios()
