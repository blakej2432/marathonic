from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from race.models import Race

def index(request):
    races = Race.objects.prefetch_related('course_type').all().order_by('date')

    return render(request, 'race/race.html', {'races': races})


def race_detail_api(request, pk):
    race = get_object_or_404(Race.objects.prefetch_related('course_type'), pk=pk)
    data = {
        "title": race.title,
        "date": race.date.strftime("%Y-%m-%d"),
        "status": "접수중" if race.regi_status == "open" else "접수 대기",
        "loc": f"{race.region}",
        "course": [ct.name for ct in race.course_type.all()],
        "homepage": race.homepage_url,
    }
    return JsonResponse(data)