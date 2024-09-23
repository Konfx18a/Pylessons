from django.db import models

# Create your models here.

class Books(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Title