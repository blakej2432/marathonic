import pandas as pd
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand

from config import settings
from race.models import CourseType, Race

COURSE_MAP = {
    "5km": "5km",
    "10km": "10km",
    "하프": "half",
    "풀": "full",
}

def determine_code(raw: str) -> str:
    for key, code in COURSE_MAP.items():
        if key.lower() == raw.lower():
            return code
    return "etc"

def parse_course_types(course_str: str):
    if pd.isna(course_str):
        return []

    course_objs = []
    raw_courses = [c.strip() for c in course_str.split(",")]

    for raw in raw_courses:
        code = determine_code(raw)
        course, _ = CourseType.objects.get_or_create(code=code, name=raw)
        course_objs.append(course)

    return course_objs

class Command(BaseCommand):
    help = "CSV 파일을 pandas로 불러와 DB에 대회 정보를 추가합니다."

    def handle(self, *args, **options):
        csv_path = Path(settings.BASE_DIR) / "race_list_2025.csv"
        try:
            df = pd.read_csv(csv_path, encoding="utf-8-sig")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"CSV 로딩 실패: {e}"))
            return

        inserted = 0
        for _, row in df.iterrows():
            try:
                title = row["대회제목"].strip()
                date = datetime.strptime(str(row["대회날짜"]).strip(), "%Y-%m-%d").date()
                region = str(row["지역"]).strip()
                course_str = str(row["코스타입"])
                homepage = str(row["홈페이지"]).strip()
                regi_status = "open" if str(row["접수중여부"]) == "접수중" else "wait"
                city = str(row["도시"]).strip()
                race = Race.objects.create(
                    title=title,
                    date=date,
                    city=city,
                    region=region,
                    regi_status=regi_status,
                    homepage_url=homepage,
                )

                course_types = parse_course_types(course_str)
                race.course_type.set(course_types)

                inserted += 1
            except Exception as e:
                self.stderr.write(self.style.WARNING(f"[실패] {title}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"{inserted}개의 대회 추가 완료."))