from django.db import models
import datetime

# Creating the model of the videos URLs

class videoLink(models.Model):
    name = models.CharField(max_length=150)
    urlVideo = models.URLField()
    bookmark = models.BooleanField(default=False)
    
 

    def __str__(self):
        return self.name
