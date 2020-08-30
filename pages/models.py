from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, blank=False, default = 'درباره ما')
    text_body = models.TextField(blank=True)

    def __str__(self):
        return self.title