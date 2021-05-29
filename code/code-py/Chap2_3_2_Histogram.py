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
# display 옵션을 이용하여 실수(소수점 3자리) 설정 - 지수표현식 해제
pd.options.display.float_format = '{:.2f}'.format


### 시각화를 위한 데이터 가공
# 2020년도 연령별 구매수량 비교
df_g = df[df['year'] == '2020'].loc[:, ['AgeGroup', 'Quantity']].copy()
df_g.head(3)

# 연령별 오름차순 정렬
ages = list(df_g['AgeGroup'].unique())
ages.sort()
ages


# https://plotly.com/python/histograms/
import plotly.graph_objects as go

# https://plotly.com/python/subplots/
from plotly.subplots import make_subplots

fig = make_subplots(rows = 2, cols = 3, shared_yaxes = 'all') # y축 공유
# = True : 동일한 row에서 처음 그려진 그래프의 y축값 공유
# = 'columns' : 동일한 column에서 처음 그려진 그래프의 y축값 공유
# = 'all' : 모든 그래프가 처음 그려진 그래프의 y축값 공유

# 20 ~ 60대 구매수량 비교
trace = []
for age in ages:
    trace.append(go.Histogram(x = df_g[df_g['AgeGroup'] == age]['Quantity'], name = age))

fig.append_trace(trace[0], 1, 1) # 위치 지정: 1행 1열
fig.append_trace(trace[1], 1, 2) # 위치 지정: 1행 2열
fig.append_trace(trace[2], 1, 3) # 위치 지정: 1행 3열
fig.append_trace(trace[3], 2, 1) # 위치 지정: 2행 1열
fig.append_trace(trace[4], 2, 2) # 위치 지정: 2행 2열
fig.update_layout(title = 'Chatper 3.2 - Histogram')
fig.show()


#
fig = make_subplots(rows = 2, cols = 2)
trace0 = go.Histogram(x = df_g[df_g['AgeGroup'] == ages[0]]['Quantity'], name = ages[0]) # 20대
trace1 = go.Histogram(x = df_g[df_g['AgeGroup'] == ages[1]]['Quantity'], name = ages[1]) # 30대
trace2 = go.Histogram(x = df_g[df_g['AgeGroup'] == ages[2]]['Quantity'], name = ages[2]) # 40대
trace3 = go.Histogram(x = df_g[df_g['AgeGroup'] == ages[3]]['Quantity'], name = ages[3]) # 50대

fig.append_trace(trace0, 1, 1) # 위치 지정
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)
fig.update_layout(title = 'Chatper 3.2 - Histogram')
fig.show()


### 누적 히스토그램
trace = go.Histogram(x = df['Quantity'], cumulative_enabled = True)
data = [trace]
fig = go.Figure(data)
fig.update_layout(title = 'Chatper 3.2 - Histogram (Cumulative)')
fig.show()

