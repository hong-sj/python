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
# 2020년도 대륙 & 채널 & 상품별 매출 Flow 오름차순 정렬
df_g = df[df['year'] == '2020'].iloc[:,[13,4,11,9]].copy()
df_g = df_g.sort_values(by = ['Region','Channel','Category'])
df_g.head(2)

value1 = df_g.groupby(by = ['Region','Channel'], as_index = False).sum()
value1

value2 = df_g.groupby(by = ['Channel','Category'], as_index = False).sum()
value2


# https://plotly.com/python/sankey-diagram/
import plotly.graph_objects as go

# label : node name (이름: 순서값을 위치값으로 이용)
# source : source node (시작 위치)
# target : target node (이동 위치)
# value : flow value (이동량)

#
trace = go.Sankey(node = dict(label = ['Africa', 'Offline', 'Online']),
                  link = dict(source = [0, 0],
                              target = [1, 2],
                              value = [4015718.1, 12342417.5])
                 )
data = [trace]
layout = go.Layout(title = 'Chapter 2.4 - Sankey Diagram', font_size = 15)
fig = go.Figure(data, layout)
fig.show()


#
trace = go.Sankey(node = dict(label = ['Africa', 'Offline', 'Online'],
                              x = [0, 1, 1],      # x 노드 위치
                              y = [0, 0.1, 0.7]   # y 노드 위치
                             ),
                  link = dict(source = [0, 0],
                              target = [1, 2],
                              value = [4015718.1, 12342417.5]),
                 )
data = [trace]
layout = go.Layout(title = 'Chapter 2.4 - Sankey Diagram (노드 위치 조정)', font_size = 15)
fig = go.Figure(data, layout)
fig.show()


#
labels = ['Africa', 'America', 'Asia', 'Europe', 'Oceania']+['Offline', 'Online']+['Beauty & Health', 'Clothes', 'Foods', 'Home', 'Office']
sources = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4] + [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
targets = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6] + [7, 8, 9, 10, 11, 7, 8, 9, 10, 11]
values = list(value1['Revenue']) + list(value2['Revenue'])

trace = go.Sankey(node = dict(label = labels,
                              pad = 15,
                              thickness = 20,
                              line = dict(color = 'black', width = 0.5),
                              color = 'blue',
                             ),
                  link = dict(source = sources,
                              target = targets,
                              value = values),
                 )
data = [trace]
layout = go.Layout(title = 'Chapter 2.4 - Sankey Diagram (노드 위치 조정)', font_size = 15)
fig = go.Figure(data, layout)
fig.show()


### label의 개수를 참조하여 source & target 자동화
# label
l_c1 = list(df_g['Region'].unique()) # 5개 (순서 = 0 1 2 3 4)
l_c2 = list(df_g['Channel'].unique()) # 2개 (순서 = 5 6)
l_c3 = list(df_g['Category'].unique()) # 5개 (순서 = 7 8 9 10 11)
labels = l_c1 + l_c2 + l_c3 # 12개 (순서 = 0 ~ 11)
print(labels)

# source
source1 = list(np.repeat(range(0, len(l_c1)), len(l_c2)))
source2 = list(np.repeat(range(len(l_c1), len(l_c1)+len(l_c2)), len(l_c3)))
sources = source1 + source2
print(sources)

# target
target1 = list(range(len(l_c1), len(l_c1)+len(l_c2))) * len(l_c1)
target2 = list(range(len(l_c1)+len(l_c2), len(l_c1)+len(l_c2)+len(l_c3))) * len(l_c2)
targets = target1 + target2
print(targets)

# value
values = list(value1['Revenue']) + list(value2['Revenue'])

trace = go.Sankey(node = dict(label = labels,
                              pad = 15,
                              thickness = 20,
                              line = dict(color = 'black', width = 0.5),
                              color = "blue"),
                  link = dict(source = sources,
                              target = targets,
                              value = values)
                 )
data = [trace]
layout = go.Layout(title = 'Chapter 2.4 - Sankey Diagram', font_size = 15)
fig = go.Figure(data, layout)
fig.show()

