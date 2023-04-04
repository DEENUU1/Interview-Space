from django.urls import path
from .views import (
    LevelList,


)

app_name = 'api'

urlpatterns = [
    path('levels', LevelList.as_view(), name='level-list'),

]