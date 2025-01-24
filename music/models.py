from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE
    )  # Reference to the Artist model
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} by {self.artist.name}"
