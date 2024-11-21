from apps.studios.models import Studio


def get_studios():
    return Studio.objects.all()
