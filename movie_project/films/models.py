from django.db import models

# Create your models here.
class Films(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'