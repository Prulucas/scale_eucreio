from django.db import models

class Music(models.Model):

    title = models.CharField("Título", max_length=50)
    ref = models.URLField("Link", max_length=200)
    description = models.CharField("Descrição", max_length=50)

    class Meta:
        verbose_name = "Música"
        verbose_name_plural = "Músicas"

    def __str__(self):
        return self.title