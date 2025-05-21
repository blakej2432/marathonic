from django.shortcuts import get_object_or_404
from race.filters import RaceFilter
from race.models import Race

class RaceService:
    @staticmethod
    def get_queryset():
        return Race.objects.prefetch_related('course_type')
    
    @classmethod
    def get_all(cls):
        return cls.get_queryset().all().order_by("date")
    
    @classmethod
    def get_by_pk(cls, pk):
        return get_object_or_404(cls.get_queryset(), pk=pk)

    @classmethod
    def get_filtered(cls, params):
        filtered = RaceFilter(params, queryset=cls.get_queryset())
        return filtered.qs.order_by("date")
