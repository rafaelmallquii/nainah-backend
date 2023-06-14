from django.db import models

# Create your models here.


class Setting(models.Model):
    site_name = models.CharField(max_length=100)
    site_description = models.TextField(max_length=200)
    site_address = models.CharField(max_length=200)
    site_phone = models.CharField(max_length=20)
    site_email = models.CharField(max_length=100)
    site_facebook = models.CharField(max_length=100)
    site_instagram = models.CharField(max_length=100)
    site_tiktok = models.CharField(max_length=100)

    site_icon = models.ImageField(upload_to='images/site/')
    site_logo = models.ImageField(upload_to='images/site/')
    site_favicon = models.ImageField(upload_to='images/site/')

    def __str__(self):
        return self.site_name


class SiteMeta(models.Model):
    setting = models.OneToOneField(Setting, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=100)
    meta_description = models.TextField(max_length=200)
    meta_keywords = models.TextField()
    meta_author = models.CharField(max_length=100)
    meta_robots = models.CharField(max_length=100)
    meta_image = models.ImageField(upload_to='images/site/')

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name_plural = 'Site Meta'
