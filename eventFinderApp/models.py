from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    categories = models.ManyToManyField('Category', related_name='events')

class Category(models.Model):
    name = models.CharField(max_length=50)
    