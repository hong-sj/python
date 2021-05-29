#!/usr/bin/env python
# coding: utf-8

# ### 라이브러리 호출

# In[1]:


import pandas as pd


# ### 데이터 호출

# In[2]:


# 상위 폴더로 이동 후 data 폴더로 이동
path = '../data/'


# In[4]:


# Sales data
sales = pd.read_csv(path + 'Sales data/Sales.csv')


# In[5]:


sales.head(2)


# In[6]:


sales.info()


# In[7]:


# Item data
item = pd.read_csv(path + 'Sales data/Item.csv')


# In[8]:


item.head(2)


# In[9]:


# Country data
country = pd.read_csv(path + 'Sales data/Country.csv')


# In[10]:


country.head(2)


# ### Merge 1. Sales & Item

# In[11]:


# sales data 복사
df = sales.copy()


# In[12]:


# data rows & columns 확인
df.shape


# In[ ]:


# pd.merge(left, right,               # merge할 DataFrame 객체 이름
#          how = 'inner',             # inner (default), left, rigth, outer
#          on = None,                # 기준이 되는 Key 변수
#          left_on = None,           # 왼쪽 DataFrame의 변수를 Key로 사용
#          right_on = None,          # 오른쪽 DataFrame의 변수를 Key로 사용
#          left_index = False,       # True이면, 왼쪽 DataFrame의 index를 merge Key로 사용
#          right_index = False,      # True이면, 오른쪽 DataFrame의 index를 merge Key로 사용
#          sort = True,              # merge된 후의 DataFrame을 join Key 기준으로 정렬
#          suffixes = ('_x', '_y'),   # 중복되는 변수 이름에 대해 접두사 부여 (defaults to '_x', '_y')
#          copy = True,              # merge할 DataFrame을 복사
#          indicator = False)        # 결합 후 DataFrame에 출처를 알 수 있는 부가 정보 변수 추가


# In[ ]:


# Key: Sales(ItemCode), Item(ItemNo)
# df = df.merge(item, how='left', left_on='ItemCode', right_on='ItemNo')
df = df.merge(item.rename(columns={'ItemNo':'ItemCode'}), on='ItemCode', how='left')


# In[ ]:


df.shape


# ### Merge 2. (Sales & Item) & Country

# In[ ]:


# Key: df(MapCode), Country(Country Code)
# df = df.merge(country, how='left', left_on='MapCode', right_on='Country Code')
df = df.merge(country.rename(columns={'Country Code':'MapCode'}), on='MapCode', how='left')


# In[ ]:


df.shape


# In[ ]:


df.head(3)


# ### csv 파일로 내보내기

# In[ ]:


df.to_csv('Sales data/Data.csv', index=None)


# In[ ]:





# In[ ]:





# In[16]:


sales.head(3)


# In[17]:


item.head(3)


# In[18]:


country.head(3)


# In[ ]:




