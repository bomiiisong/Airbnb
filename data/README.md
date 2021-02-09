# AirBnb Project Data

Airbnb Project에 사용한 데이터 설명입니다.





### accomodation_final.csv

- '여기어때' 사이트 크롤링

- `GoogleMaps API` 활용하여 숙소의 위도, 경도 정보 수집

- 변수 설명

  | Column    | 설명                 |
  | --------- | -------------------- |
  | roomID    | 숙소 상세페이지 ID   |
  | room_name | 숙소 이름            |
  | location  | 숙소 위치            |
  | link      | 숙소 상세페이지 링크 |
  | image_link | 숙소 대표 이미지 링크 |
  | latitude | 숙소 위도 정보 |
  | longitude | 숙소 경도 정보 |





### Add_2columns.csv

- '여기어때' 사이트 추가 크롤링

  1) 숙소 별 **시,도** 정보 추출

  2) **숙소 유형** 추가

| Column     | 설명                  |
| ---------- | --------------------- |
| roomID     | 숙소 상세페이지 ID    |
| room_name  | 숙소 이름             |
| location   | 숙소 위치             |
| link       | 숙소 상세페이지 링크  |
| image_link | 숙소 대표 이미지 링크 |
| latitude   | 숙소 위도 정보        |
| longitude  | 숙소 경도 정보        |
| image_link | 숙소 대표 이미지      |
| city       | 시, 도 정보           |
| accomodation_type | 숙소 유형 |



### Add_3ratings.csv

- '여기어때' 사이트 추가 크롤링(**Add_2columns.csv**에 추가)

  - 숙소의 **평점 데이터** 추가

    1) 숙소 총평

    2) 숙소 평점

    3) 숙소 리뷰 개수

  | Column            | 설명                  |
  | ----------------- | --------------------- |
  | roomID            | 숙소 상세페이지 ID    |
  | room_name         | 숙소 이름             |
  | location          | 숙소 위치             |
  | link              | 숙소 상세페이지 링크  |
  | image_link        | 숙소 대표 이미지 링크 |
  | latitude          | 숙소 위도 정보        |
  | longitude         | 숙소 경도 정보        |
  | image_link        | 숙소 대표 이미지      |
  | city              | 시, 도 정보           |
  | accomodation_type | 숙소 유형             |
  | general_review | 총평 |
  | rating | 평점 |
  | total_review_num | 총 리뷰 개수 |
