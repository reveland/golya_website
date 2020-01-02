from django.db import models
from django.urls import reverse


class Ally(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    website = models.URLField()
    facebook = models.URLField()

    def get_absolute_url(self):
        return reverse('ally-detail', kwargs={'id': self.id})
