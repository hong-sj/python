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
# 연도별 상품 매출액 합계
df_g = df.loc[:,['Category','Revenue','year']].groupby(by = ['year','Category'], as_index=False).sum()
# 매출액 별 순위 생성
df_g['Rank'] = 0
df_g.loc[df_g['Revenue']<10000000, 'Rank'] = 1
df_g.loc[(df_g['Revenue']>=10000000) & (df_g['Revenue']<30000000), 'Rank'] = 2
df_g.loc[(df_g['Revenue']>=30000000) & (df_g['Revenue']<50000000), 'Rank'] = 3
df_g.loc[(df_g['Revenue']>=50000000) & (df_g['Revenue']<70000000), 'Rank'] = 4
df_g.loc[(df_g['Revenue']>=70000000), 'Rank'] = 5
df_g.head()


# https://plotly.com/python/radar-chart/
import plotly.graph_objects as go


### 2020년도 상품 매출순위 비교
d20 = df_g[df_g['year'] == '2020'].copy().reset_index(drop = True)
trace = go.Scatterpolar(r = list(d20['Rank']),           # 평가점수
                        theta = list(d20['Category']),   # 평가항목
                        fill = 'toself',                 # 내부 음영
                        name = '2020')
data = [trace]
layout = go.Layout(title = 'Chater 3.4 - Radar Chart')
fig = go.Figure(data, layout)
fig.show()


### 마지막 부분 연결해주기
ranks = list(d20['Rank'])
ranks.append(ranks[0])
thetas = list(d20['Category'])
thetas.append(thetas[0])
print(ranks, '\n',thetas)

trace = go.Scatterpolar(r = ranks,           # 평가점수
                        theta = thetas,      # 평가항목
                        fill = 'toself',     # 내부 음영
                        name = '2020')
data = [trace]
layout = go.Layout(title = 'Chater 3.4 - Radar Chart')
fig = go.Figure(data, layout)
fig.show()


### 연도별 상품 매출순위 비교
# 연도별 오름차순 정렬
years = list(df_g['year'].unique())
years.sort()
years

traces = []
for year in years:
    dat = df_g[df_g['year'] == year] # 특정 연도 추출
    ranks = list(dat['Rank'])        # 매출 순위 리스트
    ranks.append(ranks[0])           # 마지막 연결부 추가
    thetas = list(dat['Category'])   # 상품 리스트
    thetas.append(thetas[0])         # 마지막 연결부 추가

    traces.append(go.Scatterpolar(r = ranks,
                                  theta = thetas,
                                  name = year)
                 )
data = traces
layout = go.Layout(title = 'Chater 3.4 - Radar Chart',
                   legend_orientation = "h",            # 범주 수평 나열
                   legend = dict(x = 0.3, y = -0.1),   # 범주 위치 조정
                  )

fig = go.Figure(data, layout)
fig.show()

