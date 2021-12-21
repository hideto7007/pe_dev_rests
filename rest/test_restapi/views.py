from rest_framework import generics
from rest.models.models import Actor
from rest.test_restapi.serializers import ActorSerializer


class ListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()[0:5]
    serializer_class = ActorSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
