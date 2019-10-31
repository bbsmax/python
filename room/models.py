from django.db import models
from django_countries.fields import CountryField #venv에서 pipinstall 하는것이 아니라 일반환경에서 pip install을 실행.
from core import models as core_models
from user import models as user_models


# Create your models here.
class Room(core_models.AbstractTimeStamp):
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField(default="")
    price = models.IntegerField(default=0)
    city = models.CharField(max_length=80)
    Address = models.CharField(max_length=140)
    guest = models.IntegerField()
    bedsroom = models.IntegerField()
    bathroom = models.IntegerField()
    beds = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
