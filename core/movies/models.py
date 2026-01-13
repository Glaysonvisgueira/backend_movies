from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.title
