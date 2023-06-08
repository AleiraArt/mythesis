from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year_written = models.CharField(max_length=100)
    gutenberg_id = models.IntegerField()
    flesch_kincaid_score = models.FloatField()
    difficulty = models.CharField(max_length=255)
