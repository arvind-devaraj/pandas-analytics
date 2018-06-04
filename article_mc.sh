#!/bin/sh
echo "Computing Article Details ..."

python ../article_mc.py INV.csv STORE_SALE.csv ECOM_SALE.csv ECOM_RETURN.csv FRAN_SALE.csv FRAN_RETURN.csv

echo "Merging with Hierarchy Details..."
python ../mc_merge.py ARTICLE_MC.csv ../HIERARCHY.csv