from django.db import models

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.URLField()
    pub_date = models.DateField()
    added_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

