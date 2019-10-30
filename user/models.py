from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_KOREAN = "korean"
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "kr"),
        (LANGUAGE_ENGLISH, "en"),
    )

    CURRENCY_KWD = "kwd"
    CURRENCY_USD = "usd"
    CURRENCY_CHOICES = (
        (CURRENCY_KWD, "kwd"),
        (CURRENCY_USD, "usd"),
    )

    avatar = models.ImageField(blank=True, null=True)
    bio = models.TextField(default="", blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True, null=True)
    superhost = models.BooleanField(default=False, blank=True)
    pass
