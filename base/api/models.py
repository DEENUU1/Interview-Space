from django.db import models
from django.contrib.auth.models import User

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


class Question(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    programming_lang = models.ForeignKey(ProgrammingLang, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Question'
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Comment'
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name
