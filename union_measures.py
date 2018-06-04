
 
import pandas as pd
import sys
 
list_df=[]
#keep_cols = ["Article", "ArticleDesc","BrandDescription","BrandCode", "MCDescription" , "MerCategory"]
keep_cols=["Article","Site","Dept","SOR","Quantity","NetSalesVal","COGS","Margin","SLoc","TotalSOH","TotalMAP","date"]

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
 
 

#df.drop_duplicates(subset=["Article"],keep='first',inplace=True)
 
df.to_csv("union_measures.csv", index=True)




 