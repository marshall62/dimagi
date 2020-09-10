from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50, null=True, default='ma')
    country = models.CharField(max_length=100, blank=True, default='usa')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return f"{self.email} : {self.city} @ {self.timestamp}"