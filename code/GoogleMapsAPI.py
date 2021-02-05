#!/usr/bin/env python
# coding: utf-8

# # Googlemaps API로 숙소의 위도, 경도 정보 가져오기

# In[ ]:


import googlemaps
import pandas as pd


# In[ ]:


gmaps_key = 'API설정할 때 얻은 key 값 넣기'
gmaps = googlemaps.Client(key=gmaps_key)


# In[ ]:


# data 불러오기
data = pd.read_csv('accomodation_imagelink.csv')


# In[ ]:


# location 컬럼의 숙소 위치 데이터 변수에 저장
room_location = data['location']


# In[ ]:


# Google MAp 정보 추가할 리스트 생성
accomodation_address = []     # 주소 정보
accomodation_lat = []         # 위도 
accomodation_lng = []         # 경도

for loc in room_location:                                         #숙소 위치 데이터를 순서대로 넣어서 
    tmp = gmaps.geocode(loc, language='ko')                       # geocode 함수에 파라미터로 입력 -> 위치에 맞는 지도 정보 수집(json)
    accomodation_address.append(tmp[0].get('formatted_address'))  # 수집한 정보의 0번째 요소에서 숙소 주소 정보 추출
    
    tmp_geo = tmp[0].get('geometry')                              # 위도, 경도가 포함된 요소 추출  
    accomodation_lat.append(tmp_geo['location']['lat'])           # 위도 정보 리스트에 추가 
    accomodation_lng.append(tmp_geo['location']['lng'])           # 경도 정보 리스트에 추가


for address, lat, lng in zip(accomodation_address, accomodation_lat, accomodation_lng):      #결과 출력
    print('주소: ' + address)
    print('위도: ' + str(lat) + ' 경도: ' + str(lng))
    print('---------------------------------------')


# In[ ]:


# 리스트들을 컬럼으로 추가하기 위해 data의 row 개수와 리스트 길이 동일한지 확인
print(data.shape[0])                # data row 개수 확인 

# 리스트 길이 확인 
print(len(accomodation_lat))
print(len(accomodation_lng))


# In[ ]:


# 위도, 경도 정보 컬럼으로 추가
data['latitude'] = accomodation_lat
data['longitude'] = accomodation_lng
# 결과 확인
data.head()


# In[ ]:


# 컬럼 순서 변경 (위치 정보를 모아볼 수 있도록)
data_colChage = data[['roomID', 'room_name', 'location', 'latitude', 'longitude', 'link', 'image_link']]
data_colChage.head()


# In[ ]:


# 위도, 경도 컬럼 추가한 data CSV 파일로 저장
data_colChange.to_csv('accomodation_final.csv', index=False)

