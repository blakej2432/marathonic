import django_filters

from repo.race.models import Race


class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class RaceFilter(django_filters.FilterSet):
    status = CharInFilter(field_name="regi_status", lookup_expr="in")
    city = CharInFilter(field_name="city", lookup_expr="in")
    course = CharInFilter(field_name="course_type__code", lookup_expr="in")
    date_from = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    date_to = django_filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Race
        fields = ["status", "region", "course", "date_from", "date_to"]
