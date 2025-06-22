from rest_framework import serializers
from .models import Race, CourseType


# class RaceListSerializer(serializers.ModelSerializer):
#     course_type = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Race
#         fields = [
#             "id",
#             "title",
#             "date",
#             "region",
#             "city",
#             "regi_status",
#             "race_image",
#             "course_type",
#             "homepage_url",
#         ]


class RaceListSerializer(serializers.ModelSerializer):
    course_type = serializers.StringRelatedField(many=True)
    race_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Race
        fields = [
            "id",
            "title",
            "date",
            "region",
            "city",
            "regi_status",
            "race_image",
            "course_type",
            "homepage_url",
        ]
