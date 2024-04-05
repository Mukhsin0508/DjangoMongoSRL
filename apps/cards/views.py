from django.shortcuts import render
from .models import Card
from rest_framework import serializers, viewsets

# Create your views here.

# class CardSerialalizer(serializers.ModelSerializer):
#     class Meta:
#         model = Card
#         fields = ['__All__']
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()