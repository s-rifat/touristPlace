from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='places/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Place)
def delete_image_file(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
