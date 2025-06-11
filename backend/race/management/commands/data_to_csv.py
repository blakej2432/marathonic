from django.core.management import BaseCommand
from race.models import Race
import pandas as pd

# ORM으로 모든 Race 객체 가져오기
races = Race.objects.all().prefetch_related("course_type")

# 리스트로 DataFrame 구성
data = []
class Command(BaseCommand):
    for race in races:
        data.append({
            "대회제목": race.title,
            "대회날짜": race.date.strftime("%Y-%m-%d"),
            "지역": race.region,
            "코스타입": ", ".join([c.name for c in race.course_type.all()]),
            "접수상태": race.regi_status,
            "홈페이지": race.homepage_url,
        })

    # DataFrame 생성
    df = pd.DataFrame(data)

    # CSV로 저장
    df.to_csv("race_export.csv", index=False, encoding="utf-8-sig")

    print(f"✅ 총 {len(df)}개 대회를 race_export.csv로 저장 완료.")