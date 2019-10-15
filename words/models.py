from django.db import models
from datetime import datetime


class Level(models.Model):
    Level = models.CharField(max_length=50)

    def __str__(self):
        return self.Level


class EnglishWords(models.Model):
    En_Word = models.TextField(max_length=50, null=False)
    Bn_Word = models.TextField(max_length=50, null=False)
    En_Trans = models.TextField(null=True, blank=True)
    Bn_Trans = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    Level = models.ForeignKey(
        'Level',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if len(self.En_Word) > 50:
            return self.En_Word[:50] + "..."
        return self.En_Word
