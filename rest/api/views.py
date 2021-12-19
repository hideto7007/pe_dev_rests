from rest_framework import generics
from rest.models.models import JobOffer
from rest.api.serializers import JobOfferSerializer


class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by('-id')
    serializer_class = JobOfferSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
