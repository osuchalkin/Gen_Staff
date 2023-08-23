from django.db import models

# Create your models here.
class Header(models.Model):
    """Headers"""
    text = models.CharField(max_length=200)
 
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text