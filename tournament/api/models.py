from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.year})"
