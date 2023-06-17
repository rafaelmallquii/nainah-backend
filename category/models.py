from django.db import models
from core.settings import LANGUAGE_CODE
# Create your models here.

class Category(models.Model):

    # parent if is necessary
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/categories')
    
    def __str__(self):
        return self.name
    
    class Meta:
        # cuando esta en ingles quiero un nombre plura
        if LANGUAGE_CODE == 'en':
            verbose_name_plural = 'Categories'
            verbose_name = 'Category'
        else:
            verbose_name_plural = 'Categorias'
            verbose_name = 'Categoria'

        ordering = ['name']