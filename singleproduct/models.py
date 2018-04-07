from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=250)
    album_artist = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField(max_length=1000)
    format = models.CharField(max_length=100)


class Single(models.Model):
    single_name = models.CharField(max_length=250)
    single_artist = models.CharField(max_length=250)
    single_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField(max_length=1000)