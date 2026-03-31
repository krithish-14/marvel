from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=255)
    detailed_desc = models.TextField()

    def __str__(self):
        return self.name

class Comic(models.Model):
    title = models.CharField(max_length=150)
    image_name = models.CharField(max_length=100)
    description = models.TextField()
    purchase_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title

