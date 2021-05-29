#!/usr/bin/env python
# coding: utf-8

# ### 라이브러리 호출

# In[1]:


import pandas as pd
import numpy as np


# ### 데이터 호출

# In[2]:


# 상위 폴더로 이동 후 data 폴더로 이동
path = '../data/'


# In[3]:


# 데이터 호출
df = pd.read_csv(path + 'Sales data/Data.csv')


# ### 데이터 변수 생성 및 정렬

# In[4]:


# 연도, 월 변수 생성
df['year'] = df['OrderDate'].str.slice(start = 0, stop = 4)
df['month'] = df['OrderDate'].str.slice(start = 5, stop = 7)
# 데이터 정렬
df = df.sort_values(by = ['Region','Channel','Category','Item Type','year','month','Gender'])


# ### 데이터 구조 파악

# In[5]:


df.info()


# In[ ]:





# #### 소수점 출력 설정

# In[6]:


# display 옵션을 이용하여 실수(소수점 2자리) 설정 - 지수표현식 해제
pd.options.display.float_format = '{:.2f}'.format


# In[ ]:





# ### 시각화를 위한 데이터 가공

# In[7]:


# 2020년도 이익 변수 생성
d20 = df[df['year'] == '2020'].copy()
d20['Margin'] = d20['Revenue'] - d20['Cost']


# In[8]:


# Country 별 매출 및 이익 합계 산출
df_g = d20.loc[:,['Country','Revenue','Margin']].groupby(by = ['Country'], as_index = False).sum()
df_g = df_g.sort_values(by = ['Revenue'], ascending=False)


# In[9]:


# 매출 순위 변수 (rank) 생성 후, 매출 상위 10개 Country 추출
df_g['rank'] = list(range(1, len(df_g['Country'])+1))
df_g1 = df_g[df_g['rank'] <= 10].reset_index(drop = True)
df_g1


# In[ ]:





# In[ ]:


# https://plotly.com/python/bar-charts/


# In[10]:


import plotly.graph_objects as go


# In[17]:


trace = go.Bar(x = df_g1['Country'], # x축 - 국가별
               y = df_g1['Revenue'], # y축 - 매출액
               text = round(df_g1['Revenue'],2), # text 내용(소수점 2자리 반올림)
              )
data = [trace] # data 객체에 리스트로 저장
layout = go.Layout(title = 'Chapter 2.1 - Bar Chart', width=1000, height=600) # 제목 지정
fig = go.Figure(data, layout)
fig.show()


# In[ ]:





# # 참고) 입력방식 비교

# ### Data 객체 입력 방식1. add_trace( ) 함수 이용

# In[ ]:


fig = go.Figure()
fig.add_trace(go.Bar(x = df_g1['Country'], # x축
                     y = df_g1['Revenue'], # y축
                     text = df_g1['Revenue'], # 값
                    ))
fig.update_layout(title = 'Chapter 2.1 - Bar Chart')
fig.show()


# ### Data 객체 입력 방식2. Figure( )에 직접적으로 data 객체를 정의 

# In[ ]:


fig = go.Figure(data=[
    go.Bar(x = df_g1['Country'], # x축
           y = df_g1['Revenue'], # y축
           text = round(df_g1['Revenue'],2), # 값
          )
])
fig.update_layout(title = 'Chapter 2.1 - Bar Chart')
fig.show()


# ### Data 객체 입력 방식3. data 객체를 정의한 뒤 Figure( )에 입력 

# In[14]:


trace = go.Bar(x = df_g1['Country'], # x축
               y = df_g1['Revenue'], # y축
               text = round(df_g1['Revenue'],2), # 값
              )
data = [trace] # data 객체에 리스트로 저장
layout = go.Layout(title = 'Chapter 2.1 - Bar Chart') # 제목 지정
fig = go.Figure(data, layout)
fig.show()


# In[ ]:





# In[ ]:





# # 참고) 그래프 중첩 입력방법 비교

# ### Data 객체 입력 방식1.

# In[ ]:


fig = go.Figure()
fig.add_trace(go.Bar(y = df_g1['Country'], # y축
                     x = df_g1['Revenue'], # x축
                     name = 'Revenues',
                     orientation = 'h'
                    ))
fig.add_trace(go.Bar(y = df_g1['Country'], # y축
                     x = df_g1['Margin'], # x축
                     name = 'Margins',
                     orientation = 'h'
                    ))
# Change the bar mode
fig.update_layout(title = 'Chapter 2.1 - Bar Chart', 
                  barmode = 'group',
                  yaxis = dict(autorange='reversed'))
fig.show()


# ### Data 객체 입력 방식2.

# In[ ]:


fig = go.Figure(data = [
    go.Bar(y = df_g1['Country'], # y축
           x = df_g1['Revenue'], # x축
           name = 'Revenues',
           orientation = 'h'
          ),
    go.Bar(y = df_g1['Country'], # y축
           x = df_g1['Margin'], # x축
           name = 'Margins',
           orientation = 'h'
          )
])
# Change the bar mode
fig.update_layout(title = 'Chapter 2.1 - Bar Chart', 
                  barmode = 'group',
                  yaxis = dict(autorange='reversed')) 
fig.show()


# ### Data 객체 입력 방식3.

# In[15]:


trace1 = go.Bar(y = df_g1['Country'], # y축
                x = df_g1['Revenue'], # x축
                name = 'Revenues',
                orientation = 'h'
               )
trace2 = go.Bar(y = df_g1['Country'], # y축
                x = df_g1['Margin'], # x축
                name = 'Margins',
                orientation = 'h'
               )
data = [trace1, trace2]
# Change the bar mode
layout = go.Layout(title = 'Chapter 2.1 - Bar Chart', 
                   barmode = 'group',
                   yaxis = dict(autorange='reversed'),
#                    yaxis = {'autorange':'reversed'}
                  )
fig = go.Figure(data, layout)
fig.show()

