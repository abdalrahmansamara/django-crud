from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey('auth.User', on_delete=CASCADE, default='ahmad')
    description = models.TextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse('home')
        return reverse('details', args=[str(self.id)])