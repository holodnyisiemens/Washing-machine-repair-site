from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
