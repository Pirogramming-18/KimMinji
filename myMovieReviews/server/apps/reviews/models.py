from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=64) #영화제목
    director = models.CharField(max_length=32) #감독이름
    main_actors = models.CharField(max_length=64) #주연배우들이름
    genre = models.CharField(max_length=32) #장르
    year = models.CharField(max_length=16) #개봉년도
    running_time = models.CharField(max_length=32) #러닝타임
    rating = models.CharField(max_length=32) #별점
    content = models.TextField() #리뷰텍스트