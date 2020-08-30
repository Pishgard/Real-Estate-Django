from django.db import models
from realtors.models import Realtor
from datetime import datetime

# Create your models here.


class Listings(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150, blank=True)
    address = models.TextField()
    bathroom = models.IntegerField(default=1)
    bedroom = models.IntegerField(default=1)
    infr = models.CharField(max_length=100, blank = True)
    details = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(blank=True, default=datetime.now())
    photo_main = models.ImageField(upload_to='photos/%Y/%M/%D/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%M/%D/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%M/%D/')
     
    

    def __str__(self):
        return self.title
        
