import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
	published = models.DateTimeField('date published')
	title = models.CharField(max_length = 100)
	text = models.TextField(blank=True)

'''
class Comment(modles.Model):
	name = models.CharField(max_length = 16)
	text = models.TextField
'''