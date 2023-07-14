from django.db import models

class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return f'Newsletter Template #{self.pk}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email