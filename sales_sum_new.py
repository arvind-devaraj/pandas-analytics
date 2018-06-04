
import pandas as pd
import numpy as np
import sys


outfile = "sales_sum.csv"

def process_file(infile, flag):
	df = pd.read_csv( infile, encoding='utf-8', thousands=',')
	print(df.head())
	keep_cols = ["Article", "Site", "Dept", "Quantity", "COGS", "NetSalesVal", "Margin","SOR","BillingType"]

	# SOR/BillingType fields may or maynot be present

	if not('SOR' in df.columns):
 		df['SOR']='No'

	if not('BillingType' in df.columns):
 		df['BillingType'] ='None'

	new_df = df[keep_cols]


	# if returns type, then make the quanities negative
 		
	if flag:
		print("CONSIDERING THIS FILES AS SALES ****RETURNS***** " )
		new_df.loc[:,'Quantity'] *= -1	
		new_df.loc[:,'NetSalesVal'] *= -1	
		new_df.loc[:,'COGS'] *= -1	
		new_df.loc[:,'Margin'] *= -1	


	 

	pd.to_numeric(new_df['Quantity'], errors='ignore')
	pd.to_numeric(new_df['NetSalesVal'], errors='ignore')
	pd.to_numeric(new_df['COGS'], errors='ignore')
	pd.to_numeric(new_df['Margin'], errors='ignore')

	print(new_df.head())

	# where clause - we need only Articles starting with A*

	filter_criteria = new_df['Article'].str.contains('^A', na=False)

	# fill missing values with zero
	new_df = new_df[filter_criteria ] 

	print (new_df.dtypes)
	 
	new_df['SOR'] = np.where(new_df['SOR']=='X', 'Yes', 'No')

	 
	 ###################### MOVE TO SEPARATE FILE #########################
	sum_df = new_df.groupby(['Article','Site','Dept','SOR'])['Quantity','NetSalesVal','COGS','Margin' ].sum()


	print(sum_df.head())
	 
	return sum_df
 

#start of main

list_df= []

i = 0
for arg in sys.argv:

	if(".csv" in arg):
		print ("processing..." + arg)

		#for loop on number of arguments
		#distinguish between normal&returns using some method
		#put this entire file in for loop
		#concatenate sum_df in every iteration of for loop

		infile = arg  #  eg. ecom_sale_june.csv
		returns_flag = False

		if("Return" in infile or "return" in infile or "RETURN" in infile):
			returns_flag = True


		df=process_file(infile,returns_flag)
		i = i+1
		filename = "out" +str(i)+".csv"
		df.to_csv(filename)

		list_df.append(df)

 
df_all = pd.concat(list_df)

df_all = df_all.reset_index()  
df_all = df_all.groupby(['Article','Site','Dept','SOR'])['Quantity','NetSalesVal','COGS','Margin' ].sum()

df_all.to_csv(outfile)
