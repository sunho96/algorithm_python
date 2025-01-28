from pprint import pprint

import requests # requests 라이브러리 설치 필요

# 서울시 내에 미세먼지 정보를 알 수 있다.
r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

#pprint(rjson)

rows = rjson['RealtimeCityAir']['row']
#pprint(rows)

for row in rows:
    gu_name = row['MSRSTE_NM']
    gu_mvl = row['IDEX_MVL']
    if gu_mvl < 35 :
        print(gu_name, gu_mvl)

def get_air_level(name):
    for row in rows:
        gu_name = row['MSRSTE_NM']
        gu_mvl = row['IDEX_MVL']
        if gu_name == name :
            return gu_mvl
    return "미세먼지 수치가 없습니다."

print(get_air_level('중구2'))
print(get_air_level('용산구'))
