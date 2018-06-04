
# Get Article details from inventory file
import pandas as pd
import sys
#df = pd.read_csv("test1.csv" , encoding='utf-8')

if(len(sys.argv) < 3):
	print ("Expecting <infile> <outfile1> <outfile2>")

infile = sys.argv[1]  #  eg. ecom_sale_june.csv
outfile1 = sys.argv[2]
outfile2 = sys.argv[3]

df = pd.read_csv(infile, thousands=','  )
 
#keep_cols = ["Article","Article Description", "Site","Total SOH","MAP","Brand","Brand Name","MdsceCat.","SubDepartment","Sub Department Description","Class","Class Description","SubClass","Sub Class Description","Mdse Catgry Desc."]
keep_cols = ["Article", "ArticleDesc","BrandDescription","BrandCode","MerCategory"]


#codes - Brand,MerchandiseCategory,Dept,SubDept,Class,SubClass

 

df1 = df[keep_cols]

df1.rename(columns={'ArticleDesc':'Article_Desc'}, inplace=True)
df1.rename(columns={'BrandDescription':'Brand_Desc'}, inplace=True)
#df.rename(columns={'MCDescription':'MC_Desc'}, inplace=True)
#df.rename(columns={'DeptDescription':'Dept_Desc'}, inplace=True)
#df.rename(columns={'SubDeptDescription':'SubDept_Desc'}, inplace=True)
#df.rename(columns={'ClassDescription':'Class_Desc'}, inplace=True)
#df.rename(columns={'SubClassDescription':'SubClass_Desc'}, inplace=True)

df1.rename(columns={'MerCategory':'MC'}, inplace=True)


#article_df.drop_duplicates()

# Remove duplicates  - ??? check if required / can do during union phase

#article_cols = ["Article"]  #columns to consider for removing duplicates
#grouped = df.groupby(article_cols)
#index = [gp_keys[0] for gp_keys in grouped.groups.values()]
#unique_df = 	df.reindex(index)

df1.to_csv(outfile1, index=True)




keep_cols = ["MerCategory","MCDescription","Dept","DeptDescription","SubDeptDescription","Class","ClassDescription","SubClass","SubClassDescription"]
hierarchy_df = df[keep_cols]

hierarchy_df.insert(4, "SubDept", "--")


 #hierarchy_df['MdseCatgryDesc'].str.strip()
#hierarchy_df['DepartmentDescription'].str.strip()
#hierarchy_df['SubDepartmentDescription'].str.strip()
#hierarchy_df['ClassDescription'].str.strip()
#hierarchy_df['SubClassDescription'].str.strip()


hierarchy_df.to_csv(outfile2,index=False)


