from django.db import models

# Create your models here.

class Setting(models.Model):
    site_name = models.CharField(max_length=100)

    def __str__(self):
        return self.site_name