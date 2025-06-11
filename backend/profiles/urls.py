from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='profiles-index'),
    path('login/', views.login, name='social-login')
]