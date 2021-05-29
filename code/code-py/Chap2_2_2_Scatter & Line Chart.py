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


### 데이터 변수 생성 및 정렬
# 연도, 월 변수 생성
df['year'] = df['OrderDate'].str.slice(start = 0, stop = 4)
df['month'] = df['OrderDate'].str.slice(start = 5, stop = 7)
# 데이터 정렬
df = df.sort_values(by = ['Region','Channel','Category','Item Type','year','month','Gender'])


#### 소수점 출력 설정
# display 옵션을 이용하여 실수(소수점 2자리) 설정 - 지수표현식 해제
pd.options.display.float_format = '{:.2f}'.format


### 시각화를 위한 데이터 가공
# 연도별 월 매출 현황 비교 - 연/월별 매출 합계 산출
df_g = df.loc[:,['Revenue','year','month']].groupby(by = ['year','month'], as_index = False).sum()

# 연도 오름차순 정렬
year = list(df_g['year'].unique())
year.sort()
year

df_g.head()


# https://plotly.com/python/line-and-scatter/
# https://plotly.com/python/line-charts/
import plotly.graph_objects as go


### 기본 그래프
df_g20 = df_g[df_g['year'] == '2020']
trace = go.Scatter(x = df_g20['month'],
                   y = df_g20['Revenue'],
                   mode = 'lines+markers',
                   marker = dict(size = 10),
                  )
data = [trace]
layout = go.Layout(title = 'Chapter 2.2 - Scatter & Line Charts',
                   xaxis = dict(title = 'Month'),
                   yaxis = dict(title = 'Revenue'))
fig = go.Figure(data, layout)
fig.show()


### 그래프 중첩
# Loop: 반복적으로 들어가는 year를 인자로 넣고 반복문 실행
traces = []
for years in year:
    tmp = df_g[df_g['year'] == years]
    traces.append(go.Scatter(x = tmp['month'],
                             y = tmp['Revenue'],
                             mode = 'lines+markers',
                             marker = dict(size = 10),
                             name = years
                           ))
data = traces
layout = go.Layout(title = 'Chapter 2.2 - Scatter & Line Charts',
                   xaxis = dict(title = 'Month'),
                   yaxis = dict(title = 'Revenue'))
fig = go.Figure(data, layout)
fig.show()


## 참고) 입력방식 비교
### add_trace() 방식
fig = go.Figure()
# Loop: 반복적으로 들어가는 year를 인자로 넣고 반복문 실행
for years in year:
    tmp = df_g[df_g['year'] == years]
    fig.add_trace(go.Scatter(x = tmp['month'],
                             y = tmp['Revenue'],
                             mode = 'lines+markers',
                             marker = dict(size = 10),
                             name = years
                            ))
fig.update_layout(title = 'Chapter 2.2 - Scatter & Line Charts')
fig.show()

