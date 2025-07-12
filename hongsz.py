#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[4]:


merged_df = pd.read_csv("merged.csv")


# In[7]:


st.title("レストランサーチ")

price_limit = st.slider("最低食費価格の上限",min_value=2000,max_value=25000,step=200,value=6000)
score_limit = st.slider("人気スコアの下限",min_value=0.0, max_value=100.0, step=2.0, value=5.0)


# In[8]:


filtered_df = merged_df[
    (merged_df['Average_Price(¥)']<= price_limit) &
    (merged_df['Popularity_Score']>= score_limit)
]


# In[9]:


fig = px.scatter(
    filtered_df,
    x='Popularity_Score',
    y='Average_Price(¥)',
    hover_data=['Name','Access','Rating','Reviews'],
)

st.plotly_chart(fig)


# In[10]:


selected_restrant = st.selectbox('気になるレストランを選んで詳細を確認',filtered_df['Name'])

if selected_restrant:
    url = filtered_df[filtered_df['Name'] == selected_restrant]['Tabelog_URL'].values[0]
    st.markdown(f"[{selected_restrant}のペ-ジ八移動]({url})",unsafe_allow_html=True)


# In[11]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("Rating", "Popularity_Score","Reviews","Average_Price(¥)")
)
ascending = True if sort_key == "Average_Price(¥)" else False


# In[12]:


st.subheader(f"{sort_key} によるレストランランキング(上位10件")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
# 必要な列だけ表示
st.dataframe(ranking_df[["Name","Average_Price(¥)","Popularity_Score","Rating","Reviews","Access"]])


# In[ ]:





# In[ ]:




