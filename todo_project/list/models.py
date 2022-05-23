from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class List(models.Model):
	text = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

	def was_published_recently(self):
		return self.created >= timezone.now() - datetime.timedelta(days=1)