from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='person/', blank=True)

    def __str__(self):
        return self.name
