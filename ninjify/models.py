from django.db import models
from django.utils.translation import gettext_lazy as _


class Grammar(models.TextChoices):
    ADJECTIVE = "ADJ", _('Adjective')
    NOUN = "NOUN", _('Noun')


class NinjaName(models.Model):
    label = models.CharField(max_length=255)
    type = models.CharField(
        max_length=4,
        choices=Grammar.choices,
        default=Grammar.ADJECTIVE
    )

    class Meta:
        ordering = ['type']


class Buzzword(models.Model):
    label = models.CharField(max_length=255)
    ninja_name = models.ForeignKey(NinjaName, on_delete=models.CASCADE)

    class Meta:
        ordering = ['label']
