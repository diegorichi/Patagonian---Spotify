from django.db import models


class Url(models.Model):
    spotify = models.CharField(max_length=250)
        
class Artist(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=512)
    uri = models.CharField(max_length=70)
    href = models.URLField(max_length=500, null=True)
    type = models.CharField(max_length=50)
    external_urls = models.ForeignKey(to=Url, on_delete=models.CASCADE, null=True)
    #artists = models.ForeignKey(to=Artist,  on_delete=models.SET_DEFAULT)


    def __str__(self):
        return self.name

class Song(models.Model):

    id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=512)
    artists = models.ManyToManyField(Artist)
    duration_ms = models.PositiveIntegerField()
    explicit = models.BooleanField()
    disc_number = models.PositiveSmallIntegerField()
    href = models.URLField(max_length=500, null=True)
    is_local = models.BooleanField(null=True)
    is_playable = models.BooleanField(null=True)
    preview_url = models.CharField(max_length=500, null=True)
    track_number = models.PositiveSmallIntegerField(null=True)
    type = models.CharField(max_length=20, default='truck')
    uri = models.CharField(max_length=70)
    external_urls = models.ForeignKey(to=Url, on_delete=models.CASCADE, null=True)
    #, on_delete=models.CASCADE,default='')



    def __str__(self):
        return self.name