#!/usr/bin/env python
# coding: utf-8

### 라이브러리 호출
import pandas as pd


### 데이터 호출
# 상위 폴더로 이동 후 data 폴더로 이동
path = '../data/'

# Sales data
sales = pd.read_csv(path + 'Sales data/Sales.csv')
sales.head(2)
sales.info()

# Item data
item = pd.read_csv(path + 'Sales data/Item.csv')
item.head(2)

# Country data
country = pd.read_csv(path + 'Sales data/Country.csv')
country.head(2)


### Merge 1. Sales & Item
# sales data 복사
df = sales.copy()

# data rows & columns 확인
df.shape

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

# Key: Sales(ItemCode), Item(ItemNo)
# df = df.merge(item, how='left', left_on='ItemCode', right_on='ItemNo')
df = df.merge(item.rename(columns={'ItemNo':'ItemCode'}), on='ItemCode', how='left')
df.shape


### Merge 2. (Sales & Item) & Country
# Key: df(MapCode), Country(Country Code)
# df = df.merge(country, how='left', left_on='MapCode', right_on='Country Code')
df = df.merge(country.rename(columns={'Country Code':'MapCode'}), on='MapCode', how='left')
df.shape
df.head(3)


### csv 파일로 내보내기
df.to_csv('Sales data/Data.csv', index=None)


sales.head(3)
item.head(3)
country.head(3)

