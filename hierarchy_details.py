
# compute dataframes d1 (Article, Brand, MC) and d2 (MC, Dept,SubDept,Class,SubClass)
# compute d3 from primary hierarchy file (MC, Dept,SubDept,Class,SubClass) 
# concat d2 and d3 on MC column with precedence to  primary hierarchy file as d4
# merge d1 with d4 on MC( getting (Article,Brand,MC,Dept,SubDept,Class,SubClass))

import pandas as pd
import sys
 
list_df=[]
keep_cols = ["Article", "ArticleDesc","BrandDescription","BrandCode", "MerCategory","MCDescription","Dept","DeptDescription","SubDeptDescription","SubDept", "Class","ClassDescription","SubClass","SubClassDescription"]


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


df_all = df.groupby(['Article']).last() 
df_all  = df_all.reset_index()  
print(df_all.head())



# retain and rename necessary columns 
keep_cols = ["Article", "ArticleDesc","BrandDescription","BrandCode", "MerCategory"]
df = df_all[keep_cols] 

df.rename(columns={'ArticleDesc':'Article_Desc'}, inplace=True)
df.rename(columns={'BrandDescription':'Brand_Desc'}, inplace=True)
df.rename(columns={'MerCategory':'MC'}, inplace=True)

df.to_csv("article_brand_mc.csv", index=True)





#read primary hierarchy file and remove duplicates


df_hier1 = pd.read_csv("hierarchy_conv.csv")
#article_cols = ["MC"]  #columns to consider for removing duplicates
df_hier1.drop_duplicates(["MC"])
df_hier1 = df_hier1.reindex()
keep_cols = ["MC","MC Des","Dept","Dept Des","Sub Dept","Sub Dept Des","Class","Class Des","Sub Class","Sub Class Des"]
df_hier1 = df_hier1[keep_cols]
df_hier1.to_csv("hierarchy_uniq.csv")


# secondary hierarchy from sales data files 

keep_cols = ["MerCategory","MCDescription","Dept","DeptDescription","SubDept","SubDeptDescription","Class","ClassDescription","SubClass","SubClassDescription"]
df_hier2 = df_all[keep_cols]
print(df_hier2.head())
df_hier2.rename(columns={'MerCategory':'MC'}, inplace=True)
df_hier2.rename(columns={'MCDescription':'MC Des'}, inplace=True)
df_hier2.rename(columns={'DeptDescription':'Dept Des'}, inplace=True)
df_hier2.rename(columns={'SubDept':'Sub Dept'}, inplace=True)
df_hier2.rename(columns={'SubDeptDescription':'Sub Dept Des'}, inplace=True)
df_hier2.rename(columns={'ClassDescription':'Class Des'}, inplace=True)
df_hier2.rename(columns={'SubClass':'Sub Class'}, inplace=True)
df_hier2.rename(columns={'SubClassDescription':'Sub Class Des'}, inplace=True)


#sdf_hier2.columns = ["MC","MC Des","Dept","Dept Des","Sub Dept","Sub Dept Des","Class","Class Des","Sub Class","Sub Class Des"]

article_cols = ["MC"]  #columns to consider for removing duplicates
grouped = df_hier2.groupby(article_cols)
index = [gp_keys[0] for gp_keys in grouped.groups.values()]
df_hier2 = 	df_hier2.reindex(index)
df_hier2.to_csv("hierarchy_sec.csv")

#combine both hierarchies, giving priority to primary hierarchy (using keep=first parameter)

df_hier1.reset_index(drop=True, inplace=True)
df_hier2.reset_index(drop=True, inplace=True)

hier_all = pd.concat([df_hier1,df_hier2])

hier_all.drop_duplicates(subset=["MC"],keep='first',inplace=True)
hier_all = hier_all.reindex()
hier_all.to_csv("hier_all.csv")