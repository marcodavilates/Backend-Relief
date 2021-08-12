from django.db import models

# Creating the model of the videos URLs

class videoLink(models.Model):
    name = models.CharField(max_length=150)

    #urlVideo is primary key because have to times the same URL is a waste of memory
    urlVideo = models.URLField(primary_key=True)
    bookmark = models.BooleanField(default=False)

    def __str__(self):
        return self.name
