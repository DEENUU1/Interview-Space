from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    name = models.CharField(max_length=20)
    short_desc = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'level'
        verbose_name_plural = 'levels'

    def __str__(self):
        return self.name


class ProgrammingLang(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    short_desc = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Programming language'
        verbose_name_plural = "Programming languages"

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now=True)
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


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='favourites')

    class Meta:
        ordering = ('question',)
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return self.user.username
