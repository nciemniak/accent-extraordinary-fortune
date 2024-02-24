from django.db import models

class Zodiac(models.Model):
  year = models.IntegerField(default=0)
  element = models.CharField(max_length=200)
  animal = models.CharField(max_length=200)
  start_date = models.DateField()
  end_date = models.DateField()
