from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=64)
    director = models.CharField(max_length=32)
    main_actors = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    year = models.CharField(max_length=16)
    running_time = models.CharField(max_length=32)
    rating = models.CharField(max_length=32)
    content = models.TextField()