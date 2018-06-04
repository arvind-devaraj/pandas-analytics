

import pandas as pd
import numpy as np
import sys

 
df = pd.read_csv( "measures.csv", encoding='utf-8', thousands=',')

pd.to_numeric(df['Quantity'], errors='ignore')
pd.to_numeric(df['NetSalesVal'], errors='ignore')
pd.to_numeric(df['COGS'], errors='ignore')
pd.to_numeric(df['Margin'], errors='ignore')

pd.to_numeric(df['TotalSOH'], errors='ignore')
pd.to_numeric(df['TotalMAP'], errors='ignore')
df.rename(columns={'Department':'Dept'}, inplace=True)

print(df.head())
TOPN=50

df_DA = df.groupby(['Dept','Article','date']).sum().reset_index().sort(['Dept', 'NetSalesVal'], ascending=[1,0])
df_SA = df.groupby(['Site','Article','date']).sum().reset_index().sort(['Site', 'NetSalesVal'], ascending=[1,0])
df_DSA = df.groupby(['Dept','Site','Article','date']).sum().reset_index().sort(['Dept','Site', 'NetSalesVal'], ascending=[1,1,0]) 

#writing top Dept/Article
keep_cols=['Dept','Article','NetSalesVal','Quantity','COGS','Margin','TotalSOH','TotalMAP','date']
df_DA = df_DA[keep_cols]
df_DA = df_DA.groupby(['Dept']).head(TOPN)
df_DA.to_csv("topm_dept.csv")



keep_cols=['Site','Article','NetSalesVal','Quantity','COGS','Margin','TotalSOH','TotalMAP','date']
df_SA= df_SA[keep_cols]
df_SA = df_SA.groupby(['Site']).head(TOPN)
df_SA.to_csv("topm_store.csv")
print(df_SA.head())

keep_cols=['Dept','Site','Article','NetSalesVal','Quantity','COGS','Margin','TotalSOH','TotalMAP','date']
df_DSA=df_DSA[keep_cols]
df_DSA = df_DSA.groupby(['Dept','Site']).head(10)

df_DSA.to_csv("topm_dept_store.csv")
 