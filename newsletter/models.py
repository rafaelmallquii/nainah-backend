from django.db import models

class Newsletter(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return f'Newsletter Template #{self.pk}'

class Subscriber(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email