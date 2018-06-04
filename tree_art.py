#tree

import pandas as pd
import sys

df_measures = pd.read_csv("measures.csv")
 
df_m = df_measures.groupby(['Article'])['Quantity','NetSalesVal','COGS','Margin','TotalSOH','TotalMAP'].sum()

 
df_m.to_csv("temp.csv")
df_m = pd.read_csv("temp.csv")

  

df_ad = pd.read_csv("article_details.csv",index_col=0)
 

#df_mc = pd.read_csv("MC_MEASURES.csv")
df = pd.merge(df_ad,df_m,on=['Article'],how='right')

 #keep_cols = ['Dept_Desc_Code','SubDept_Desc_Code','Class_Desc_Code','SubClass_Desc_Code', 'MC_Desc_Code','MC', 'Brand_Name_Code','Quantity','NetSalesVal','COGS','Margin','TotalSOH','TotalMAP']

#df = df[keep_cols] 


df['date'] = df_measures.iloc[0]['date']
df.to_csv("article_measures.csv")
 

  
#print(df.head())
