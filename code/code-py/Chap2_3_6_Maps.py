#!/usr/bin/env python
# coding: utf-8

### 라이브러리 호출
import pandas as pd
import numpy as np


### 데이터 호출
# 상위 폴더로 이동 후 data 폴더로 이동
path = '../data/'

# 데이터 호출
df = pd.read_csv(path + 'Sales data/Data.csv')

# 연도, 월 변수 생성
df['year'] = df['OrderDate'].str.slice(start = 0, stop = 4)
df['month'] = df['OrderDate'].str.slice(start = 5, stop = 7)
# 데이터 정렬
df = df.sort_values(by = ['Region','Channel','Category','Item Type','year','month','Gender'])


#### 소수점 출력 설정
# display 옵션을 이용하여 실수(소수점 3자리) 설정 - 지수표현식 해제
pd.options.display.float_format = '{:.2f}'.format


### 시각화를 위한 데이터 가공
# 2020년도 데이터 추출
df_g = df[df['year']=='2020'].copy()
# 국가별 매출 합계 : 수치 출력 조정 (10만 단위)
df_g1 = df_g.loc[:,['Country','Revenue']].groupby(by = ['Country'], as_index=False).sum()
# 국가별 고유 좌표값
df_map = df.loc[:,['Country','Longitude','Latitude','Code3']].drop_duplicates()
# 국가별 매출 데이터와 좌표 결합
df_g2 = df_g1.merge(df_map, on = 'Country', how = 'left')
# 출력 문구 생성
df_g2['text'] = df_g2['Country'] + ' - Total Revenue : ' +                 round(df_g2['Revenue']/1000000,1).astype(str) + 'M'
df_g2.head()


# https://plotly.com/python/bubble-maps/
import plotly.graph_objects as go


### Bubble Map - go.Scattergeo
trace = go.Scattergeo(lat = df_g2['Latitude'],   # 위도
                      lon = df_g2['Longitude'],  # 경도
                      mode = 'markers',          # 산점도
                      marker = dict(symbol = 'circle',  # 원형
                                    size = np.sqrt(df_g2['Revenue']/10000)), # 원형 크기 조정
                      text = df_g2['text'],      # hover text 활성화
                      hoverinfo = 'text',        # 입력한 text만 활성화
                     )
data = [trace]
layout = go.Layout(title = 'Chapter 3.6 - Bubble Maps',
                   geo = dict(scope = 'world',
                              projection_type = 'equirectangular',
                              showcountries = True))   # 지도 경계선
fig = go.Figure(data, layout)
fig.show()


### Choropleth Map - go.Choropleth
trace = go.Choropleth(locations = df_g2['Code3'], # 국가코드 (영역)
                      z = df_g2['Revenue'],       # 영역 내 표현 값
                      colorscale = 'Blues',       # 영역 색상
                #     autocolorscale = True,      # 컬러바 구성 scale 자동화
                      reversescale = True,          # 컬러바 scale 명암 반대
                      marker_line_color = 'darkgray',   # 영역 테두리 색상
                      marker_line_width = 0.5,          # 영역 테두리 두께
                      colorbar_tickprefix = '$',      # 컬러바 축 문자열
                      colorbar_title = 'Revenue US$') # 컬러바 제목
data = [trace]
layout = go.Layout(title = 'Chapter 3.6 - Choropleth Maps',
                   geo=dict(scope = 'world',
                            projection_type = 'equirectangular',
                            showframe = False,       # 지도 테두리
                            showcoastlines = False)) # 해안 경계선
fig = go.Figure(data, layout)
fig.show()


### Map style - projection_type 종류
# equirectangular
# mercator
# orthographic
# natural earth
# kavrayskiy7
# miller
# robinson
# eckert4
# azimuthal equal area
# azimuthal equidistant
# conic equal area
# conic conformal
# conic equidistant
# gnomonic
# stereographic
# mollweide
# hammer
# transverse mercator

