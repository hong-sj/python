#!/usr/bin/env python
# coding: utf-8

# plotly.express
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'],
                 title = 'plotly.express')
fig.show()


# plotly.graph_objects
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=df[df['species']=='setosa']['sepal_width'],
                         y=df[df['species']=='setosa']['sepal_length'],
                         mode='markers',
                         name='setosa',
                         marker=dict(color='#6973FB',
                                     size=df[df['species']=='setosa']['petal_length']*10)
                        ))
fig.add_trace(go.Scatter(x=df[df['species']=='versicolor']['sepal_width'],
                         y=df[df['species']=='versicolor']['sepal_length'],
                         mode='markers',
                         name='versicolor',
                         marker=dict(color='#F1644D',
                                     size=df[df['species']=='versicolor']['petal_length']*5)
                        ))
fig.add_trace(go.Scatter(x=df[df['species']=='virginica']['sepal_width'],
                         y=df[df['species']=='virginica']['sepal_length'],
                         mode='markers',
                         name='virginica',
                         marker=dict(color='#29C99F',
                                     size=df[df['species']=='virginica']['petal_length']*4.6)
                        ))
fig.update_layout(xaxis = dict(title='sepal_width'),
                  yaxis = dict(title='sepal_length'),
                  legend_title_text='species',
                  title = 'plotly.graph_objects'
                 )
fig.show()

