from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

STATUS = ((0, 'Waiting Confirmation'), (1, 'Published'))

class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    

    def __str__(self):
        # return f"{self.name} in {self.city}"
        return self.name

class Gig(models.Model):
    # fakedate = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.venue} at {self.date}'


class Release(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    release = models.ManyToManyField(Release)

    def __str__(self):
        return self.title


class Setlist(models.Model):
    gig = models.OneToOneField(Gig, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='setlist_author')
    song = models.ManyToManyField(Song)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.gig}"


