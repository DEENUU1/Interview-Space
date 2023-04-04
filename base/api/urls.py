from django.urls import path
from .views import (
    LevelList,
    QuestionList,

)

app_name = 'api'

urlpatterns = [
    path('levels/', LevelList.as_view(), name='level-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),




]