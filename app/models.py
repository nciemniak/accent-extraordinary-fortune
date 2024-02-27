from django.db import models
from django.utils import timezone

class Zodiac(models.Model):
  year = models.IntegerField(default=0)
  element = models.CharField(max_length=200)
  animal = models.CharField(max_length=200)
  start_date = models.DateField()
  end_date = models.DateField()
  trait_1 = models.CharField(max_length=200, default="")
  trait_2 = models.CharField(max_length=200, default="")

  @property
  def image_url(self):
    return f"app/images/zodiac_animals/{self.element.lower()}_{self.animal.lower()}.jpeg"
  
  @property
  def title(self):
    text = f"{self.element} {self.animal}!"
    return text.upper()
  

class Image(models.Model):
    image = models.ImageField(upload_to='app/static/app/images/temp')
    type = models.CharField(max_length=200) # user photo or ai generation?
