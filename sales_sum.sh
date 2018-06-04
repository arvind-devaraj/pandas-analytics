#!/bin/sh
echo "Computing Sales measures..."

python ../sales_sum_new.py STORE_SALE.csv ECOM_SALE.csv ECOM_RETURN.csv FRAN_SALE.csv FRAN_RETURN.csv

wc STORE_SALE.csv ECOM_SALE.csv ECOM_RETURN.csv FRAN_SALE.csv FRAN_RETURN.csv
wc out1.csv out2.csv out3.csv out4.csv out5.csv
