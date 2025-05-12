from django.shortcuts import render

def index(request):
    return render(request, 'race/my_race.html')