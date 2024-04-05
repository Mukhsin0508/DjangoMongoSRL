from django.shortcuts import render
from .models import Deck
from rest_framework import serializers, viewsets

# Create your views here.

# class CardSerialalizer(serializers.ModelSerializer):
#     class Meta:
#         model = Card
#         fields = ['__All__']

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'

class DecksViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()