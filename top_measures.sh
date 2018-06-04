cd april
python ../top_measures.py 
cd ..
cd may
python ../top_measures.py 
cd ..
cd june
python ../top_measures.py 
cd ..
cd july
python ../top_measures.py 
cd ..
cd august
python ../top_measures.py 
cd ..

#merge into single file 
awk 'FNR==1 && NR!=1{next;}{print}' april/topm_dept.csv may/topm_dept.csv june/topm_dept.csv july/topm_dept.csv august/topm_dept.csv > union_topm_dept.csv
awk 'FNR==1 && NR!=1{next;}{print}' april/topm_store.csv may/topm_store.csv june/topm_store.csv july/topm_store.csv august/topm_store.csv > union_topm_dept.csv
awk 'FNR==1 && NR!=1{next;}{print}' april/topm_dept_store.csv may/topm_dept_store.csv june/topm_dept_store.csv july/topm_dept_store.csv august/topm_dept_store.csv > union_topm_dept.csv

