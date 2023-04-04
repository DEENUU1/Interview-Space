from django.urls import path
from .views import (
    LevelList,
    QuestionList,
    ProgrammingLangList,
    QuestionCreateView,
    CommentList,
    AddToFavourite,

)

app_name = 'api'

urlpatterns = [
    path('levels/', LevelList.as_view(), name='level-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('languages/', ProgrammingLangList.as_view(), name='languages-list'),
    path('comments/', CommentList.as_view(), name='commants-list'),
    path('questions/<int:question_id>/favourites/', AddToFavourite.as_view(), name='add-to-favourite'),
    




]