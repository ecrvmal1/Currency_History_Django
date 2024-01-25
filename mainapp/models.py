import datetime as datetime
from django.db import models


class Rate(models.Model):
    datetime = models.DateTimeField(auto_now_add=True )
    currency = models.CharField(max_length=16)
    rate = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()