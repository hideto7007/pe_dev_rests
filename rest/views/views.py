from rest_framework import viewsets
from rest.models.models import Actor
from rest.serializer.serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    """ActorオブジェクトのCRUD"""
    queryset = Actor.objects.first()
    print(queryset)
    # serializer_class = ActorSerializer
