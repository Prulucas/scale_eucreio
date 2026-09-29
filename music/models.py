from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField("Título", max_length=50)

    class Meta:
        verbose_name = "Música"
        verbose_name_plural = "Músicas"

    def __str__(self):
        return self.title