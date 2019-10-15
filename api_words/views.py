from rest_framework import generics

from words.models import EnglishWords
from words.models import Level

from .serializers import EnglishWordSerializer
from .serializers import LevelSerializer


class QuoteAPIView(generics.ListAPIView):
    queryset = EnglishWords.objects.all()
    serializer_class = EnglishWordSerializer


class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnglishWords.objects.all()
    serializer_class = EnglishWordSerializer


class QuoteAPINewView(generics.ListCreateAPIView):
    queryset = EnglishWords.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = EnglishWordSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

