from django.db import models

# Create your models here.

class URLDB(models.Model):
    originalUrl = models.CharField(max_length = 255,unique=True)
    shortenedUrl = models.CharField(max_length = 6,unique=True)
    def __str__(self):
        return self.originalUrl
