from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title