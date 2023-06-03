from django.db import models

class Own(models.Model):
    name = models.CharField(max_length=120)
    package = models.IntegerField()
    drug = models.CharField(max_length=120)
    phone = models.IntegerField()
    address = models.CharField(max_length=1000)