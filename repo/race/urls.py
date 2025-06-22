from django.urls import path
from .views import race_views, myrace_views

urlpatterns = [
    path("", race_views.index, name="race-index"),
    path("detail/<int:pk>/", race_views.race_detail_api, name="race-detail-api"),
    path("my_race", myrace_views.index, name="my-race"),
    path("race_list/", race_views.RaceListAPIView.as_view(), name="race-list"),
]
