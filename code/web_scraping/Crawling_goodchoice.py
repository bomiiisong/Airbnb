#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


# # location -> 시,군,구 통합

# In[ ]:


# 각 변수 담을 리스트
room_id = []
room_name = []
room_location = []
room_link = []
idx_list = []

# 700 page crawling
for page in range(700):
    roomID = str(50000+page)  
    link = 'https://www.goodchoice.kr/product/detail?ano=' + roomID   #임의의 roomID부터 차례로 300개 검색
    
    url = requests.get(link)
    url = url.text
    
    soup = BeautifulSoup(url, 'html.parser')
    
    infos = soup.select('div.right')  # <div class="right"> 하위의 값을 가져와라
    
    for info in infos:
        name = info.select_one('h2').text   #infos 하위의 <h2> 태그에 있는 값 중 텍스트만 선택해서 저장
        room_name.append(name)              # room_name 리스트에 추가
        
        location = info.select_one('p.address').text    # infos 하위의 <p class="address"> 의 값 중 텍스트만 선택해서 저장
        room_location.append(location)                  # room_location 리스트에 추가
        
        room_id.append(roomID)                          # room_id 추출하기 위해 리스트에 저장 
        room_link.append(link)                          # room_link 추출하기 위해 리스트에 저장
        
        time.sleep(3)   # 잠시 멈추기
        
for idx, value in enumerate(room_name):     # 정보가 없는 숙소의 roomID 찾기 위해 room_name의 index 이용
    if not room_name[idx]:
        idx_list.append(idx)        
    else:
        pass
    
idx_list = list(reversed(idx_list))       # room_name의 index 순서대로 삭제하면, loop 할 때마다 index 순서가 앞당겨짐
                                          # (리스트 요소가 삭제되면서 index가 조정되기 때문)
                                          # 따라서 reversed() 함수로 index 역순으로 변경 -> 다시 list 형태로 저장

for n in idx_list:     # 역순으로 각 리스트 요소 삭제
    del room_id[n]
    del room_name[n]
    del room_location[n]
    del room_link[n]

# print(room_id)
# print(room_name)
# print(room_location)
# print(room_link)


# In[ ]:


accomodation_base = pd.DataFrame({'roomID' : room_id, 'room_name': room_name, 'location' : room_location, 'link' : room_link})
accomodation_base.to_csv('accomodation_base.csv', index=False)


# # Image Link 컬럼 추가

# In[ ]:


# accomodation_base.csv 불러오기
df = pd.read_csv("accomodation_base.csv")
# roomID만 저장
col = df['roomID']


# In[ ]:


#image Link 가져오기

image_link = []   # 이미지 링크 추가할 리스트 생성

for page in col: # roomID 저장한 변수 차례대로 불러오기
    
    roomID = str(page)  # 해당하는 pasge 번호 저장
    link = 'https://www.goodchoice.kr/product/detail?ano=' + roomID  # 링크 저장

    # request. beautifulsoup으로 html 불러오기
    url = requests.get(link)
    url = url.text
    soup = BeautifulSoup(url, 'html.parser')
    
    # 숙소 정보가 포함된 selector를 활용하여 값 검색
    img_selector = soup.findAll('div', {'class' : 'gallery_m'})
    
    # 불러온 숙소 정보 중 0번째 값의 <img> 태그만 선택
    img = img_selector[0].find('img')
    # <img> 태그 안의 실제 이미지 링크를 포함하고 있는'data-src' 값 저장
    img_source = img.get('data-src')
    
    # 리스트에 추가
    image_link.append(img_source)


# In[ ]:


# image_link 리스트를 컬럼으로 추가하기 위해 data의 row 개수와 image_link 리스트 길이 동일한지 확인
print(df.shape)          # data shape 확인
print(len(image_link))   # image_link 리스트 길이 확인


# In[ ]:


# image_link -> data 컬럼으로 추가
df['image_link'] = image_link
# 결과 확인
df.head()


# In[ ]:


# image_link 컬럼 추가한 data CSV 파일로 저장
df.to_csv('accomodation_imagelink.csv', index=False)

