from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 30)
	sub_title = models.CharField(max_length = 15)
	author = models.CharField(max_length = 10)
	text = models.TextField()