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
# 이익(Margin) 생성
df['Margin'] = df['Revenue'] - df['Cost']
# 2020년도 매출 및 이익
df_g = df[df['year']=='2020'].copy()
# 수치 출력 조정 (10만 단위)
df_g1 = round(df_g.loc[:,['Revenue','Margin']].sum()/1000000,2)
df_g1


# https://plotly.com/python/indicator/
import plotly.graph_objects as go

trace1 = go.Indicator(value = 200,
                      delta = dict(reference = 160),
                      gauge = dict(axis = dict(visible = False)),
                      domain = dict(row = 0, column = 0))
trace2 = go.Indicator(value = 120,
                      gauge = dict(shape = 'bullet'),
                      domain = dict(x = [0.05, 0.5], y = [0.15, 0.35]))
trace3 = go.Indicator(mode = 'number+delta',
                      value = 300,
                      domain = dict(row = 0, column = 1))
trace4 = go.Indicator(mode = 'delta',
                      value = 40,
                      domain = dict(row = 1, column = 1))
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(grid = {'rows': 2, 'columns': 2, 'pattern' : 'independent'},
                   template = {'data' : {'indicator' : 
                                         [{'title' : {'text' : 'Speed'},
                                           'mode' : 'number+delta+gauge',
                                           'delta' : {'reference': 90}}]}})
fig = go.Figure(data, layout)
fig.show()


#
values = df_g1['Revenue']
deltas = df_g1['Revenue'] - df_g1['Margin']
trace = go.Indicator(mode = 'number+delta',                           # 출력 방식
                     value = values,                                  # 주요값 입력
                     number = dict(prefix = '$',                      # 주요값 앞 문자열
                                   suffix = 'M',                      # 주요값 뒤 문자열
                                   valueformat = ',0f'),              # 값 형식
                     delta = dict(reference = deltas,                 # 차이값 입력
                                  valueformat = '.2f',                # 값 형식
                                  relative = False,
                                  increasing = dict(color = 'blue'),  # 증가 시 색상
                                  position = 'top'))                  # 차이값 위치 
data = [trace]
layout = go.Layout(title = 'Chatper 3.5 - Indicator',
                   paper_bgcolor = "white")                           # 배경 흰색
fig = go.Figure(data, layout)
fig.show()


