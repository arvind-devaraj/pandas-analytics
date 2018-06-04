import pandas as pd

df_hier1 = pd.read_csv("hierarchy_uniq.csv")
df_hier2 = pd.read_csv("hierarchy_sec.csv")

#http://stackoverflow.com/questions/32801806/pandas-concat-ignore-index-doesnt-work

df_hier1.reset_index(drop=True, inplace=True)
df_hier2.reset_index(drop=True, inplace=True)

hier_all = pd.concat([df_hier1,df_hier2])

hier_all.drop_duplicates(subset=["MC"],keep='first',inplace=True)
hier_all = hier_all.reindex()
hier_all.to_csv("hier_all.csv")

