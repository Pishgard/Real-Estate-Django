from django.db import models
from datetime import datetime

class Order(models.Model):
    listing_name = models.CharField(max_length=50, blank=False, null=True)
    listing_id = models.IntegerField(blank=False)
    client_email = models.CharField(max_length=40, blank=False, null=True)
    client_name = models.CharField(max_length=50, blank=False, null=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    checking = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name