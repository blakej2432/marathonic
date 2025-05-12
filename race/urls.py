from django.urls import path
from .views import race_views, myrace_views

urlpatterns = [
    path('', race_views.index, name='race-index'),
    path('my_race', myrace_views.index, name='my-race'),
]