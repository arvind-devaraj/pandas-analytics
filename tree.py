#tree

import pandas as pd
import sys

df_m = pd.read_csv("measures.csv")
df_a = pd.read_csv("ARTICLE_MC.csv")

df = pd.merge(df_m, df_a, on=['Article' ],how='outer')
#df.to_csv("temp.csv")
print(df.head(5))
df_mc = df.groupby(['MC','BrandCode','Brand_Desc'])['Quantity','NetSalesVal','COGS','Margin','TotalSOH','TotalMAP'].sum()
df_mc.to_csv("MC_MEASURES.csv")


df_h = pd.read_csv("../HIERARCHY.csv")
 
df_h['MC_Desc_Code'] = df_h['MC Des'].astype(str) + " - " + df_h['MC']
df_h['Dept_Desc_Code'] =    df_h['Dept Des'].astype(str).str.strip() + " - " + df_h['Dept']
df_h['SubDept_Desc_Code'] = df_h['Sub Dept Des'].astype(str).str.strip() + " - " + df_h['Sub Dept']
df_h['Class_Desc_Code'] = df_h['Class Des'].astype(str).str.strip()  + " - " + df_h['Class']
df_h['SubClass_Desc_Code'] = df_h['Sub Class Des'].astype(str).str.strip()  + " - " + df_h['Sub Class']



df_mc = pd.read_csv("MC_MEASURES.csv")
df = pd.merge(df_h,df_mc,on=['MC'],how='outer')
df['Brand_Name_Code'] =  df['Brand_Desc'].astype(str).str.strip()  + " - " + df['BrandCode']

keep_cols = ['Dept_Desc_Code','SubDept_Desc_Code','Class_Desc_Code','SubClass_Desc_Code', 'MC_Desc_Code','MC', 'Brand_Name_Code','Quantity','NetSalesVal','COGS','Margin','TotalSOH','TotalMAP']

df = df[keep_cols] 


df['date'] = df_m.iloc[0]['date']
df.to_csv("tree.csv")
 

  
#print(df.head())
