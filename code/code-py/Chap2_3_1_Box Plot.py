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
# 2020년도 대륙별 매출액 비교
df_g = df[df['year'] == '2020'].loc[:,['Region','Revenue']].copy()
df_g.head(3)

# 대륙별 오름차순 정렬
regions = list(df_g['Region'].unique())
regions.sort()
regions


# https://plotly.com/python/box-plots/
import plotly.graph_objects as go

# Loop: 반복적으로 들어가는 regions를 인자로 넣고 반복문 실행
traces = []
for region in regions:
    tmp = df_g[df_g['Region'] == region]
    traces.append(go.Box(y = tmp['Revenue'], name = region))
data = traces
layout = go.Layout(title = 'Chapter 3.1 - Box Plot')
fig = go.Figure(data, layout)
fig.show()


# 
d_1 = df_g[df_g['Region'] == regions[0]]
d_2 = df_g[df_g['Region'] == regions[1]]
d_3 = df_g[df_g['Region'] == regions[2]]
d_4 = df_g[df_g['Region'] == regions[3]]
d_5 = df_g[df_g['Region'] == regions[4]]

trace1 = go.Box(y = d_1['Revenue'], name = regions[0])
trace2 = go.Box(y = d_2['Revenue'], name = regions[1])
trace3 = go.Box(y = d_3['Revenue'], name = regions[2])
trace4 = go.Box(y = d_4['Revenue'], name = regions[3])
trace5 = go.Box(y = d_5['Revenue'], name = regions[4])
trace6 = go.Box(boxpoints = 'all', jitter = 0)

data = [trace1, trace2, trace3, trace4, trace5, trace6]
layout = go.Layout(title = 'Chapter 3.1 - Box Plot')
fig = go.Figure(data, layout)
fig.show()

