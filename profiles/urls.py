from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/", include("allauth.urls"), name="socialaccount_signup"),
    path('', views.index, name='profiles-index'),
]