"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls"), name="socialaccount_signup"),
    path("race/", include("repo.race.urls")),
    path("profiles/", include("repo.profiles.urls")),
    # path('shoes/', include('repo.shoes.urls')),
    path("", RedirectView.as_view(url="/race")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__", include("debug_toolbar.urls")),
    ]
