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
# Asia 내의 Foods 상품 데이터 추출
df1 = df[(df['Region'] == 'Asia') & (df['Category'] == 'Foods')].copy()

# 채널별 연도 평균 매출 추이 비교
df_g = df1.loc[:,['Channel','year','Revenue']].copy()
# 상품/연도별 매출 통계량 계산 & 결과 결합
g_mean = df_g.groupby(by = ['Channel','year'], as_index = False).mean()  # 평균
g_std = df_g.groupby(by = ['Channel','year'], as_index = False).std()    # 표준편차
g_n = df_g.groupby(by = ['Channel','year'], as_index = False).count()    # 개수
df_g1 = pd.concat([g_mean.reset_index(drop = True),
                   g_std['Revenue'].reset_index(drop = True),
                   g_n['Revenue'].reset_index(drop = True)],
                   axis = 1)
df_g1.columns = ['Channel','year','mean','sd','n']   # 변수명 변경
df_g1


# https://plotly.com/python/error-bars/
import plotly.graph_objects as go


### 오프라인 매출 추이 비교
df_g2 = df_g1[df_g1['Channel'] == 'Offline'].copy()

trace = go.Scatter(x = df_g2['year'],
                   y = df_g2['mean'],
                   error_y = dict(type = 'data',             # 실제 값 이용. 'percent'는 비율 기준
                                  array = df_g2['sd'],       # 중심값 대비 상한/하한 차이값
                                 ),
                   name = 'Offline'
                  )
data = [trace]
layout = go.Layout(title = 'Chapter 3.3 - Scatter & Error Bar (Offline)',
                   xaxis = dict(title = 'Year'),
                   yaxis = dict(title = 'Revenue (Mean)'))
fig = go.Figure(data, layout)
fig.show()


### Tips. 축 최대/최소 & hover text 조정
# 상한값, 하한값 생성 
df_g1['lower'] = df_g1['mean'] - df_g1['sd']
df_g1['upper'] = df_g1['mean'] + df_g1['sd']
# 축 범위 - 최소값 및 최대값 계산
import math
ymax = math.ceil(df_g1['upper'].max()*1.05)
ymin = math.ceil(df_g1['lower'].min()*0.95)

# hover text 입력 -> 평균값 (하한값, 상한값)
df_g1['text'] = (df_g1['mean']/1000).round(2).apply(lambda x: str(x)) + 'K (' +                 (df_g1['lower']/1000).round(2).apply(lambda x: str(x)) + 'K, ' +                 (df_g1['upper']/1000).round(2).apply(lambda x: str(x)) + 'K)'
df_g1.head(3)

# 채널 참조리스트 생성
channels = list(df_g1['Channel'].unique())
# 빈 리스트 생성
traces = []
for channel in channels:
    dat = df_g1[df_g1['Channel'] == channel]
    traces.append(go.Bar(x = dat['year'],
                         y = dat['mean'],
                         error_y = dict(type = 'data',
                                        array = dat['sd']
                                       ),
                         text = dat['text'],  # hover text 활성화
                         name = channel
                        ))
data = traces
layout = go.Layout(title = 'Chapter 3.3 - Bar & Error Bar',
                  xaxis = dict(title = 'Year'),
                  yaxis = dict(title = 'Revenue (Mean)', range = [0, ymax]))
fig = go.Figure(data, layout)
fig.show()


# 채널 참조리스트 생성
channels = list(df_g1['Channel'].unique())
# 빈 리스트 생성
traces = []
for channel in channels:
    dat = df_g1[df_g1['Channel'] == channel]
    traces.append(go.Bar(x = dat['year'],
                         y = dat['mean'],
                         error_y = dict(type = 'data',
                                        symmetric = False,  # 비대칭 / True: 대칭(default)
                                        array = dat['sd']
                                       ),
                         text = dat['text'],  # hover text 활성화
                         hoverinfo = 'text',  # 입력한 text만 활성화
                         name = channel
                        ))
data = traces
fig = go.Figure(data)
layout = go.Layout(title = 'Chapter 3.3 - Bar & Error Bar',
                  xaxis = dict(title = 'Year'),
                  yaxis = dict(title = 'Revenue (Mean)', range = [0, ymax]))
fig = go.Figure(data, layout)
fig.show()

