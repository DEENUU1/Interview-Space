from django.urls import path
from .views import (
    LevelList,
    QuestionList,
    ProgrammingLangList,




)

app_name = 'api'

urlpatterns = [
    path('levels/', LevelList.as_view(), name='level-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('languages/', ProgrammingLangList.as_view(), name='languages-list'),




]