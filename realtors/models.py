from django.db import models

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    facebook = models.CharField(max_length=25, blank=True)
    photo_main = models.ImageField(upload_to='profile/%Y/%M/%D/', blank=True)

    def __str__(self):
        return self.name 