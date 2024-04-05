from django.db import models
from apps.decks.models import Deck

# Create your models here.

class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.question