import pandas as pd
import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]
df_art = pd.read_csv(infile1)
df_hier = pd.read_csv(infile2)

# merge article df and hierarch on MC column

df = pd.merge(df_art, df_hier, on=['MC' ],how='outer')


#MC|MC Des|Dept|Dept Des|Sub Dept|Sub Dept Des|Class|Class Des|Sub Class|Sub Class Des
df.fillna('--')
print (df.head())
print (df.dtypes)
df['MC_Desc_Code'] = df['MC Des'].astype(str) + " - " + df['MC']
 
df['Dept_Desc_Code'] =    df['Dept Des'].astype(str).str.strip() + " - " + df['Dept']
df['SubDept_Desc_Code'] = df['Sub Dept Des'].astype(str).str.strip() + " - " + df['Sub Dept']
df['Class_Desc_Code'] = df['Class Des'].astype(str).str.strip()  + " - " + df['Class']
df['SubClass_Desc_Code'] = df['Sub Class Des'].astype(str).str.strip()  + " - " + df['Sub Class']


df['Brand_Name_Code'] = df['Brand_Desc'].astype(str).str.strip()  + " - " + df['BrandCode']

 
keep_cols = ["Article","Article_Desc","Dept_Desc_Code","SubDept_Desc_Code" ,"Brand_Name_Code","MC_Desc_Code","Class_Desc_Code","SubClass_Desc_Code"]

df=df[keep_cols]  

print(df.head())

df.to_csv("article_details.csv", index=True)



