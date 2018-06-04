import pandas as pd
import sys

infile = sys.argv[1]

df = pd.read_csv(infile, thousands=','  )
 
#keep_cols = ["Article","Article Description", "Site","Total SOH","MAP","Brand","Brand Name","MdsceCat.","SubDepartment","Sub Department Description","Class","Class Description","SubClass","Sub Class Description","Mdse Catgry Desc."]

keep_cols = ["Article", "Site", "SLoc", "Department","TotalSOH", "TotalMAP" ]
new_df = df[keep_cols]
new_df.rename(columns={'Department':'Dept'}, inplace=True)

#new_df.to_csv("inv_proj1.csv", index=False)


# Extract (Article,Site)--> TotalSOH, TotalMAP 
sum_df = new_df.groupby(['Article','Site','SLoc' ,"Dept"])['TotalSOH','TotalMAP' ].sum()
print( sum_df.head())

sum_df.to_csv("inv_sum.csv", index=True)



#group_by_site
sum_df = new_df.groupby(['Site' ])['TotalSOH','TotalMAP' ].sum()
print( sum_df.head())
sum_df.to_csv("inv_sum_by_site.csv", index=True)



#group_by_site
sum_df = new_df.groupby(['Dept' ])['TotalSOH','TotalMAP' ].sum()
print( sum_df.head())
sum_df.to_csv("inv_sum_by_dept.csv", index=True)

df1 = new_df.loc[new_df['Site']==6301]
keep_cols=['Article','TotalMAP']
df2 = df1[keep_cols]
df2.to_csv("6301articles.csv")

print(df1.count())
