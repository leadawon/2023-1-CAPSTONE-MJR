from django.db import models

# Create your models here.

class menu(models.Model):
    foodname = models.CharField(max_length=30)
    restname = models.CharField(max_length=30)

    lat = models.CharField(max_length=20, null=True, blank=True)
    lon = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.foodname








