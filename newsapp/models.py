from django.db import models

# Create your models here.
class NewsLink(models.Model):
		name = models.CharField(max_length=200)
		rss = models.URLField(max_length=200)