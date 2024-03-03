from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, default="Title")
    content = models.CharField(max_length=1000, default="Content")
    name = models.CharField(max_length=100,default="Name")
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="images", default="")
    youtubelink = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.title

class Banners(models.Model):
    titleline1 = models.CharField(max_length=200, default="Title")
    titleline2 = models.CharField(max_length=200, default="Title")
    subtitle = models.CharField(max_length=200, default="SubTitle")
    description = models.CharField(max_length=200, default="Description")
    buttontext = models.CharField(max_length=200, default="Button Text")
    buttonhref = models.CharField(max_length=200, default="Button Href")
    image = models.ImageField(upload_to="images", default="")
    def __str__(self):
        return self.titleline1