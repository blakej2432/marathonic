import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "http://www.roadrun.co.kr/schedule/list.php"
response = requests.get(url)
response.encoding = 'euc-kr'  # 또는 'euc-kr' 시도 (확인 필요)
response
soup = BeautifulSoup(response.text, 'html.parser')
soup

target_table = soup.select('body > p > table > tr:nth-of-type(3) > td > p:nth-of-type(2) > table > tr > td > table:nth-of-type(3)')
target_table = soup.select('body > p > table > tr:nth-of-type(3) >td')
target_table
p = target_table[0].find('p', attrs={'align': 'left'})
trs = p.select('table > tr > td > table:nth-of-type(3) >tr')

trs
race_data = []


for tr in trs:
    try:
        tds = tr.find_all('td')
        if len(tds) < 4:
            continue  # 필드가 부족하면 스킵

        # 날짜 추출 및 포맷 변경
        # date_raw = tds[0].get_text(strip=True).split('(')[0].strip()  # "5/3"
        date_raw = tds[0].get_text()
        try:
            date_obj = datetime.strptime(date_raw, "%m/%d")
            race_date = f"2025-{date_obj.month:02}-{date_obj.day:02}"  # 연도는 임의 설정
        except:
            continue  # 날짜 형식이 이상하면 건너뜀

        # 접수중 여부 확인 (접수중이면 <img> 있음)
        is_open = bool(tds[0].find('img'))

        # 대회명
        race_title = tds[1].find('a').get_text(strip=True)

        # 코스 타입
        course_font = tds[1].find('font', attrs={'color': '#990000'})
        course_type = course_font.get_text(strip=True) if course_font else ''

        # 지역
        location = tds[2].get_text(strip=True)

        # 홈페이지 url
        home_url = ''
        for a in tds[3].find_all('a', href=True):
            if a['href'].startswith('http'):
                home_url = a['href']
                break

        race_data.append({
            "대회제목": race_title,
            "대회날짜": race_date,
            "지역": location,
            "코스타입": course_type,
            "접수중여부": "접수중" if is_open else "",
            "홈페이지": home_url
        })

    except Exception as e:
        # 디버깅 필요하면 print(e)
        continue

print(race_data)
# CSV로 저장
df = pd.DataFrame(race_data)

df.to_csv("marathon_schedule_2025.csv", index=False, encoding='utf-8-sig')
print("✅ CSV 저장 완료! 항목 수:", len(df))

