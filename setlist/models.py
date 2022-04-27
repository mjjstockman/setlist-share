from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Waiting Confirmation'), (1, 'Published'))

class Gig(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Song(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Setlist(models.Model):
    gig = models.OneToOneField(Gig, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.gig.city