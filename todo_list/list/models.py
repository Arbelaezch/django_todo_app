from django.db import models

import datetime

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BinaryField(default=False)

    def __str__(self):
        return self.title