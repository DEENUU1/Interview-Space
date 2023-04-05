from django.urls import path
from .views import (
    LevelList,
    QuestionList,
    ProgrammingLangList,
    QuestionCreateView,
    CommentList,
    AddToFavourite,
    FavouriteDelete,

)

app_name = 'api'

urlpatterns = [
    path('levels/', LevelList.as_view(), name='level-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('languages/', ProgrammingLangList.as_view(), name='languages-list'),
    path('comments/', CommentList.as_view(), name='commants-list'),
    path('favourites/<int:question_id>/', AddToFavourite.as_view(), name='add-to-favourite'),
    path('favourites/<int:question_id>/', FavouriteDelete.as_view(), name='delete-from-favourites')




]