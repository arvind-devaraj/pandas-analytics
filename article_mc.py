
# compute dataframes d1 (Article, Brand, MC) and d2 (MC, Dept,SubDept,Class,SubClass)
# compute d3 from primary hierarchy file (MC, Dept,SubDept,Class,SubClass) 
# concat d2 and d3 on MC column with precedence to  primary hierarchy file as d4
# merge d1 with d4 on MC( getting (Article,Brand,MC,Dept,SubDept,Class,SubClass))

import pandas as pd
import sys
 
list_df=[]
keep_cols = ["Article", "ArticleDesc","BrandDescription","BrandCode", "MCDescription" , "MerCategory"]


# read each CSV file into individual dataframe (df_each) and concat them as single df
for arg in sys.argv:

	if(not(".csv" in arg)):
		continue;

	print ("processing..." + arg)

	#concatenate df in every iteration of for loop
	df_each = pd.read_csv(arg, thousands=','  )
	df_each = df_each[keep_cols]
 
	print(df_each.head()) 
	list_df.append(df_each)

 
df = pd.concat(list_df)
 
# filter articles beginning with A 
filter_criteria = df['Article'].str.contains('^A', na=False)
df = df[filter_criteria ] 


#df_all = df.groupby(['Article']).last() 
#df_all  = df_all.reset_index()  
#print(df_all.head())
 

df.drop_duplicates(subset=["Article"],keep='first',inplace=True)
df['MCDescription']  = df['MCDescription'].str.strip()
df['ArticleDesc']  = df['ArticleDesc'].str.strip()
df['BrandDescription'] =df['BrandDescription'].str.strip()
df['MCDescription'] = df['MCDescription'].str.strip()

df.rename(columns={'ArticleDesc':'Article_Desc'}, inplace=True)
df.rename(columns={'BrandDescription':'Brand_Desc'}, inplace=True)
df.rename(columns={'MerCategory':'MC'}, inplace=True)

df.to_csv("ARTICLE_MC.csv", index=True)




 