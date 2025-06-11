from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from race.models import Race
from race.services import RaceService

def index(request):
    races = RaceService.get_filtered(request.GET)
    return render(request, 'race/race.html', {'races': races})


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