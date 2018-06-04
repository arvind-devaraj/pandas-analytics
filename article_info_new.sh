#!/bin/sh

#no spaces around =
STORE_SALE="Stores_July_2016.csv"
ECOM_SALE="Ecom_Sale_July2016.csv"
ECOM_RETURN="Ecom_Return_July2016.csv"
FRAN_SALE="Franch_July_Sales.csv"
FRAN_RETURN="Franch_July_Returns.csv"



INV="inventory1.csv"
echo "converting file formats..."
set -x
 
#iconv -f utf-8 -t utf-8 -c  "$INV" -o  "$INV.new"
iconv -f utf-8 -t utf-8 -c  "$STORE_SALE" -o  "$STORE_SALE.new"
iconv -f utf-8 -t utf-8 -c   "$ECOM_SALE" -o "$ECOM_SALE.new"
iconv -f utf-8 -t utf-8 -c   "$ECOM_RETURN" -o "$ECOM_RETURN.new"
iconv -f utf-8 -t utf-8 -c  "$FRAN_SALE" -o  "$FRAN_SALE.new"
iconv -f utf-8 -t utf-8 -c  "$FRAN_RETURN" -o  "$FRAN_RETURN.new"


echo "Headers of inventory"
#Name,ArticleDescription,Article,Site,SLoc,TotalSOH,TotalMAP,BlockedQty,BlockedValue,Department,DepartmentDescription,Brand,BrandName,Seas,SeasonDescription,ProductType,MRP,MdseCat,SiteType,SubDepartment,SubDepartmentDescription,Class,ClassDescription,SubClass,SubClassDescription,MdseCatgryDesc
new_header="Name,ArticleDesc,Article,Site,SLoc,TotalSOH,TotalMAP,BlockedQty,BlockedValue,Dept,DeptDescription,BrandCode,BrandDescription,Seas,SeasonDescription,ProductType,MRP,MerCategory,SiteType,SubDept,SubDeptDescription,Class,ClassDescription,SubClass,SubClassDescription,MCDescription"
sed -i.bak "1 s/^.*$/$new_header/" "$INV.new"


echo "Headers of Store "

 #reading Article, Quantity, NetSalesVal, MAPValue as COGS, Data as BillingDate
new_header="Site,StoreName,BillingDate,Article,ArticleDesc,Quantity,NetSalesVal,MRP,SOR,GrossSales,COGS,SORBrandMargin,Margin,DiscountValue,BrandCode,BrandDescription,MerCategory,MCDescription,Dept,DeptDescription,SubDept,SubDeptDescription,Class,ClassDescription,SubClass,SubClassDescription,Season,SeasonDesc,Salesdistrict,RoyaltyRate"
sed -i.bak "1 s/^.*$/$new_header/" "$STORE_SALE.new"


echo "Headers of ECOM "
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,ECOMOrderNo,SoldtoParty,CST Amt,NameSoldtoParty,City,Article,ArticleDesc,HandlingCharges,Quantity,MRP,VATAmt,GSV,DiscountValue,COGS Amount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,ServiceTax,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetRoyalty,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" "$ECOM_SALE.new"


#  Sales Org,Item No,Billing Date,UOM,Billing Doc,ECOM Order No,Sold to Party,CST Amt,Name-Sold to Party,City,Article,Article Desc,Handling Charges,Billed quantity,       MRP,  VAT Amt,       GSV,Discount Value,COGS Amount,Brand Description,MC Description,Total MAP value,Industry Des,Brand Code,Mer. Category,  MAP/unit,Billing Type,OBD NO,Industry,Sales District,Product Hierarchy,SAP Sales Order,Sub Dept Description,Billing A/c Doc,Billing Cancel/not,Delivery A/c Doc,Tax Code,Site,SLoc,Service Tax,Sub Class,Sub Class Description,Dept,Dept Description,Class,Class Description,Payer,Total Sale Value,Season,Net Royalty,Net Sales Value


echo "Headers of ECOM-Returns"
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,ECOMOrderNo,SoldtoParty,CST Amt,NameSoldtoParty,City,Article,ArticleDesc,HandlingCharges,Quantity,MRP,VATAmt,GSV,DiscountValue,COGS Amount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,ServiceTax,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetRoyalty,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" "$ECOM_RETURN.new"
         
echo "Headers of Franchise "  
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,SoldtoParty,CSTAmt,NameSoldtoParty,City,Article,ArticleDesc,Quantity,MRP,VATAmt,BasicPrice,DiscountValue,COGSAmount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" "$FRAN_SALE.new"


echo "Headers of Franchise Returns "  
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,SoldtoParty,CSTAmt,NameSoldtoParty,City,Article,ArticleDesc,Quantity,MRP,VATAmt,BasicPrice,DiscountValue,COGSAmount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" "$FRAN_RETURN.new"


echo "Computing Sales article_details..."
python article_details.py  "$STORE_SALE.new" "$ECOM_SALE.new" "$ECOM_RETURN.new" "$FRAN_SALE.new" "$FRAN_RETURN.new"

         
echo "Done.."

#python inv_ad.py inventory1.csv inv_article_details.csv inv_hier_details.csv


#sed 1d inv_hier_details.csv > inv_hier_details_temp.csv
#sed 1d sales_hier_details.csv > sales_hier_details_temp.csv 
#cat hierarchy1.csv inv_hier_details_temp.csv sales_hier_details_temp.csv > hierarchy_all.csv

#python union_article_details.py 


#python inv_sum.py "$INV.new" inv_sum.csv


#echo "Merge Sales and Inventory measures"
#python merge.py 


#get article details sales_ad
#get inventory details inv_ad
#union of those

#convert pipe separated to comma
#merge


