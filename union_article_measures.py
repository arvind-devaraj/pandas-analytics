
 
import pandas as pd
import sys
 
list_df=[]
#keep_cols = ["Article", "Article_Desc","Dept_Desc_Code","SubDept_Desc_Code", "Brand_Name_Code" , "MC_Desc_Code", "Class_Desc_Code","SubClass_Desc_Code"]


# read each CSV file into individual dataframe (df_each) and concat them as single df
for arg in sys.argv:

	if(not(".csv" in arg)):
		continue;

	print ("processing..." + arg)

	#concatenate df in every iteration of for loop
	df_each = pd.read_csv(arg, thousands=',',index_col=0  )
	#df_each = df_each[keep_cols]
 
	print(df_each.head()) 
	list_df.append(df_each)

 
df = pd.concat(list_df)
 
 
print(df.head())
#df.drop_duplicates(subset=["Article"],keep='first',inplace=True)
 

df.to_csv("union_article_measures.csv", index=True)




 