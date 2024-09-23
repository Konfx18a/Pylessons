from django.db import models

# Create your models here.

class Books(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Title
