import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.binary_location = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"

################

driver = webdriver.Chrome(options=options)

coffee_types={1010: "싱글오리진", 1020: "블렌딩", 1030: "디카페인"}
data = []

for coffee_type in coffee_types.keys():
    base_url = f"https://cuppingcoffee.kr/shop/list.php?ca_id={coffee_type}&&page="
    page_num = 1

    while True:
        url = base_url + str(page_num)
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "item-row"))
            )
        except Exception as e:
            print(f"Timeout or no items found on page {page_num}")
            break

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        items = soup.find_all('div', class_='item-row')
        print(page_num)
        print(items)

        if not items:
            break
        
        product_urls = []

        for item in items:
            product_link_tag = item.find('a', href=True)
            if product_link_tag:
                product_url = "https://cuppingcoffee.kr/shop" + product_link_tag['href'].lstrip('.')
                product_urls.append(product_url)

        page_num += 1
        time.sleep(1)

        for product_url in product_urls:
            driver.get(product_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            bean_title = soup.find('div', class_='bean_title').h3.text.strip() if soup.find('div', class_='bean_title') else None
            
            cupping_note = soup.find('div', class_='bean_ta_text').p.text.strip() if soup.find('div', class_='bean_ta_text') else None
            
            detail_info = {}
            info_section = soup.find('div', class_='bean_detail_info')
            if info_section:
                items = info_section.find_all('li')
                for item in items:
                    title = item.find('span', class_='title').text.strip()
                    text = item.find('span', class_='text').text.strip()
                    detail_info[title] = text
                    
            tasting_info = {
                '산미': None,
                '바디감': None,
                '단맛': None,
                '로스팅': None,
                '쓴맛': None
            }

            tasting_section = soup.find('div', class_='coffee_bean_ta_box')
            if tasting_section:
                tasting_items = tasting_section.find_all('li')
                for item in tasting_items:
                    title = item.find('em', class_='title_1').text.strip()
                    class_value = item['class'][0]  # 예: li_3
                    value = int(class_value.split('_')[1])  # 숫자 값만 추출
                    if title in tasting_info:
                        tasting_info[title] = value

            data.append({
                '원두타입': coffee_types[coffee_type],
                '원두명': bean_title,
                '노트': cupping_note,
                **detail_info,
                **tasting_info
            })
            time.sleep(0.5)

len(product_urls)
driver.quit()

df = pd.DataFrame(data)
len(df)
df.to_csv('coffee_beans_info.csv', index=False, encoding='utf-8-sig')


example = str(soup)
with open("example.txt", "w") as file:
    file.write(example)

print("문자열이 성공적으로 저장되었습니다.")