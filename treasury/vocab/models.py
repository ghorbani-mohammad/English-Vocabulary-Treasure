from django.db import models

from user.models import Profile
from reusable.models import BaseModel


class Vocabulary(BaseModel):
    expression = models.CharField(max_length=20, unique=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vocabularies"


class ProfileVocabulary(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Profile Vocabularies"
