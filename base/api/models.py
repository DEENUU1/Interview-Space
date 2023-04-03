from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    short_desc = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'level'
        verbose_name_plural = 'levels'

    def __str__(self):
        return self.name


class ProgrammingLang(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    short_desc = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Programming language'
        verbose_name_plural = "Programming languages"

    def __str__(self):
        return self.name
    
