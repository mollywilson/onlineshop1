from django.db import models


class Earrings(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField(max_length=1000)


class Rings(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField(max_length=1000)
    size = models.CharField(max_length=50)
    collection = models.ForeignKey(Earrings, on_delete=models.CASCADE)
