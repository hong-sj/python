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
# 2020년도 연령별 매출액 비교
df_g = df[df['year'] == '2020'].copy()

# 연령별 매출 합계 산출
df_g1 = df_g.loc[:,['AgeGroup','Revenue']].groupby(by = ['AgeGroup'], as_index = False).sum()
df_g1


# https://plotly.com/python/pie-charts/
import plotly.graph_objects as go

#
trace = go.Pie(labels = df_g1['AgeGroup'],
               values = df_g1['Revenue']
              )
data = [trace]
layout = go.Layout(title = 'Chapter 2.3 - Pie Chart')
fig = go.Figure(data, layout)
fig.show()


#
trace = go.Pie(labels = df_g1['AgeGroup'],
               values = df_g1['Revenue'],
               pull = [0, 0, 0.2, 0, 0] # label 순서와 동일 (0~1 범위)
              )
data = [trace]
layout = go.Layout(title = 'Chapter 2.3 - Pie Chart Split')
fig = go.Figure(data, layout)
fig.show()


#
trace = go.Pie(labels = df_g1['AgeGroup'],
               values = df_g1['Revenue'],
               textinfo = 'label+percent',             # text 값
               insidetextorientation = 'tangential',   # testinfo 타입 (tangential / auto / horizontal / radial)
               hole = 0.4,                             # 원 중심부 구멍 크기
              )
data = [trace]
layout = go.Layout(title = 'Chapter 2.3 - Pie Chart Hole')
fig = go.Figure(data, layout)
fig.show()

