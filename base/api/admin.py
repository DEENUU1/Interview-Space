from django.contrib import admin
from .models import Level, ProgrammingLang, Question, Comment, Favourite, Category

admin.site.register(Level)
admin.site.register(ProgrammingLang)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Favourite)
admin.site.register(Category)
