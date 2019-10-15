from rest_framework import serializers

from words.models import EnglishWords
from words.models import Level


class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWords
        # ('__all__')  for all fields
        # ['quote', 'author']
        # fields = ['quote', 'author']
        fields = ('__all__')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        # ('__all__')  for all fields
        # ['title']
        fields = ('__all__')