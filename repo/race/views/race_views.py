from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from repo.race.filters import RaceFilter
from repo.race.models import Race
from repo.race.services import RaceService
from repo.race.serializers import RaceListSerializer


def index(request):
    races = RaceService.get_filtered(request.GET)
    return render(request, "race/race.html", {"races": races})


def race_detail_api(request, pk):
    race = RaceService.get_by_pk(pk)
    data = {
        "title": race.title,
        "date": race.date.strftime("%Y-%m-%d"),
        "status": "접수중" if race.regi_status == "open" else "접수 대기",
        "loc": f"{race.region}",
        "course": [ct.name for ct in race.course_type.all()],
        "homepage": race.homepage_url,
    }
    return JsonResponse(data)


class RaceListAPIView(APIView):
    def get(self, request, *args, **kawrgs):
        queryset = RaceService.get_filtered(request.query_params)
        serializer = RaceListSerializer(queryset, many=True)
        return Response(serializer.data)
