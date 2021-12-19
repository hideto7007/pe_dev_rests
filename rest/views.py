from django.shortcuts import render
from rest_framework import viewsets
from rest.models.models import Actor
from rest.serializer.serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    """ActorオブジェクトのCRUD"""
    queryset = Actor.objects.all().order_by('-created_at')
    serializer_class = ActorSerializer
