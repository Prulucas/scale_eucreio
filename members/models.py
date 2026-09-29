from django.db import models


class Member(models.Model):
    first_name = models.CharField("Primeiro Nome", max_length=50)
    last_name = models.CharField("Último Nome", max_length=50)

    is_minister = models.BooleanField("É Ministro", default=False)
    is_musician = models.BooleanField("É Músico", default=False)
    is_backing_vocal = models.BooleanField("É Backing Vocal", default=False)
    description = models.CharField("Descrição", max_length=50)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"