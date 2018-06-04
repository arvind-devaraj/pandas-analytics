
import pandas as pd
import sys
sales_df = pd.read_csv("sales_sum.csv")
inv_df = pd.read_csv("inv_sum.csv")

mdate = sys.argv[1]
# get sales measures and inventory measures joined by (Article,Site)
measure_df = pd.merge(sales_df, inv_df, on=['Article','Site','Dept' ],how='outer')

print(measure_df.head())

# avoid converting to float
measure_df['Site'] = measure_df['Site'].astype(int)

measure_df['date'] = mdate

#measure_df['Sloc'] = ''

#duplicates considering columns Article and Site and SOR ( those duplicates caused by inventory SLoc)
is_duplicate = measure_df.groupby(["Article","Site","SOR"]).cumcount()

#set Quantity,NetSalesVal,COGS,Margin to zero for duplicates
measure_df['NetSalesVal'][is_duplicate>0] = 0
measure_df['COGS'][is_duplicate>0] = 0
measure_df['Margin'][is_duplicate>0] = 0
measure_df['Quantity'][is_duplicate>0] = 0

#duplicates considering columns Article and Site and SLoc ( those duplicates caused by Sales table-SOR)

is_duplicate = measure_df.groupby(["Article","Site","SLoc"]).cumcount()
measure_df['TotalMAP'][is_duplicate>0] = 0
measure_df['TotalSOH'][is_duplicate>0] = 0


measure_df.to_csv("measures.csv", index=True)


  
 
