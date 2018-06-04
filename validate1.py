
import pandas as pd


#STORE_SALE="Stores_July_2016.csv.new"
#ECOM_SALE="Ecom_Sale_July2016.csv.new"
#FRAN_SALE="Franch_July_Sales1.XLS.csv.new"


#df1 = pd.read_csv(STORE_SALE)
#df2 = pd.read_csv(ECOM_SALE)
#df3 = pd.read_csv(FRAN_SALE)

#df = pd.concat([df1,df2,df3])

df = pd.read_csv("sales_sum.csv")

article_group = df.groupby(['Article'])['Quantity'  ].sum()
site_group = df.groupby(['Site'])['Quantity'  ].sum()
print(article_group.head())
article_group.to_csv("article_group_in.csv") 
site_group.to_csv("site_group_in.csv") 


# may have to read from 3 different files and union
df = pd.read_csv("measures.csv")


dept_grp=  df.groupby(['Dept']).count()
print (dept_grp.head(50)) 

article_group = df.groupby(['Article'])['Quantity' ].sum()
article_group.to_csv("article_group2.csv")

site_group = df.groupby(['Site'])['Quantity' ].sum()
site_group.to_csv("site_group2.csv")


#inv_group = df.groupby(['Site'])['TotalMAP' ].sum()
#inv_group.to_csv("inv_group1.csv")
 

  
 