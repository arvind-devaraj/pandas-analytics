#!/bin/sh

#no spaces around =
INV=$1
STORE_SALE=$2
ECOM_SALE=$3
ECOM_RETURN=$4
FRAN_SALE=$5
FRAN_RETURN=$6


echo "converting file formats..."
set -x
 
 
iconv -f utf-8 -t utf-8 -c  "$STORE_SALE" -o  STORE_SALE.csv
iconv -f utf-8 -t utf-8 -c   "$ECOM_SALE" -o  ECOM_SALE.csv
iconv -f utf-8 -t utf-8 -c   "$ECOM_RETURN" -o ECOM_RETURN.csv
iconv -f utf-8 -t utf-8 -c  "$FRAN_SALE" -o  FRAN_SALE.csv
iconv -f utf-8 -t utf-8 -c  "$FRAN_RETURN" -o  FRAN_RETURN.csv
iconv -f utf-8 -t utf-8 -c  "$INV" -o INV.csv

#note : column names  in header should not contain spaces or special characters

echo "Headers of Store "

# add error checking that compares headers of original and new files

 #reading Article, Quantity, NetSalesVal, MAPValue as COGS, Data as BillingDate
new_header="Site,StoreName,BillingDate,Article,ArticleDesc,Quantity,NetSalesVal,MRP,SOR,GrossSales,COGS,SORBrandMargin,Margin,DiscountValue,BrandCode,BrandDescription,MerCategory,MCDescription,Dept,DeptDescption,SubDept,SubDeptDescription,Class,ClassDescription,SubClass,SubClassDescription,Season,SeasonDesc,Salesdistrict,RoyaltyRate"
sed -i.bak "1 s/^.*$/$new_header/" STORE_SALE.csv


echo "Headers of ECOM "
 #reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SaleOrg,ItemNo,BillingDate,UOM,BillingDoc,ECOMOrderNo,SoldtoParty,CSTAmt,NameSoldtoParty,City,Article,ArticleDesc,Quantity,MRP,VATAmt,GSV,DiscountValue,COGS Amount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" ECOM_SALE.csv


echo "Headers of ECOM-Returns"
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SaleOrg,ItemNo,BillingDate,UOM,BillingDoc,ECOMOrderNo,SoldtoParty,CSTAmt,NameSoldtoParty,City,Article,ArticleDesc,Quantity,MRP,VATAmt,GSV,DiscountValue,COGS Amount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetSalesVal,Margin"

#new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,ECOMOrderNo,SoldtoParty,CST Amt,NameSoldtoParty,City,Article,ArticleDesc,HandlingCharges,Quantity,MRP,VATAmt,GSV,DiscountValue,COGS Amount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,ServiceTax,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetRoyalty,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" ECOM_RETURN.csv

echo "Headers of Franchise "  
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,PONumber,SoldtoParty,CSTAmt,NameSoldtoParty,City,Article,ArticleDesc,Quantity,MRP,VATAmt,BasicPrice,DiscountValue,COGSAmount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" FRAN_SALE.csv

echo "Headers of Franchise Returns "  
#reading Article,Billedquantity as Quantity,TotalMAPalue as COGS
new_header="SalesOrg,ItemNo,BillingDate,UOM,BillingDoc,PONumber,SoldtoParty,CSTAmt,NameSoldtoParty,City,Article,ArticleDesc,Quantity,MRP,VATAmt,BasicPrice,DiscountValue,COGSAmount,BrandDescription,MCDescription,COGS,IndustryDes,BrandCode,MerCategory,MAPunit,BillingType,OBDNO,Industry,SalesDistrict,ProductHierarchy,SAPSalesOrder,SubDeptDescription,SubDept,BillingAcDoc,BillingCancelnot,DeliveryAcDoc,TaxCode,Site,SLoc,SubClass,SubClassDescription,Dept,DeptDescription,Class,ClassDescription,Payer,TotalSaleValue,Season,NetSalesVal,Margin"
sed -i.bak "1 s/^.*$/$new_header/" FRAN_RETURN.csv

echo "Headers of Inventory"
#new_header="Name,ArticleDesc,Article,Site,SLoc,TotalSOH,TotalMAP,BlockedQty,BlockedValue,Department,DepartmentDescription,BrandCode,BrandDescription,Seas,SeasonDescription,ProductType,MRP,MerCategory,SiteType,SubDepartment,SubDepartmentDescription,Class,ClassDescription,SubClass,SubClassDescription,MCDescription"
#for apr

#            Article,ArticleDescription,Name1,Site,SLoc,TotalSOH,TotalMAP,MdseCat.,Transit/Transf.,Val.inTrans./Tfr,BlockedQty,BlockedValue,Department,DepartmentDescription,Brand,BrandName,Seas,SeasonDescription,PRODUCTTYPE,MRP,SiteType,SubDepartment,SubDepartmentDescription,Class,ClassDescription,SubClass,SubClassDescription,MdseCatgryDesc.
		
new_header="Article,ArticleDesc,Site,SLoc,TotalSOH,TotalMAP,BlockedQty,BlockedValue,MerCategory,MCDescription,Department,DepartmentDescription,SubDepartment,SubDepartmentDescription,Class,ClassDescription,SubClass,SubClassDescription,BrandCode,BrandDescription,Seas,SeasDes,SiteDesc,SiteType,ProductType"
          
#new_header="ArticleDescription,Name1,Article,Site,SLoc,TotalSOH,TotalMAP,BlockedQty,BlockedValue,BrandCode,BrandDescription,Seas,Season Description,PRODUCT TYPE,MRP,Site Type,Department,SubDepartmentDescription,DepartmentDescription,SubDepartment,Class,ClassDescription,SubClass,SubClassDescription,MCDescription,MerCategory"
              
#may
new_header="Article,ArticleDesc,Site,SLoc,TotalSOH,TotalMAP,MerCategory,BlockedQty,BlockedValue,Department,DepartmentDescription,SubDepartment,SubDepartmentDescription,Class,ClassDescription,SubClass,SubClassDescription,MCDescription,BrandCode,BrandDescription,Seas,SeasDesc,PRODUCTTYPE,MRP,SiteType"

#sep

new_header="Article,ArticleDesc,Name1,Site,SLoc,TotalSOH,TotalMAP,MerCategory,BlockedQty,BlockedValue,Department,DepartmentDescription,Brand,BrandName,Seas,SeasonDescription,PRODUCTTYPE,MRP,SiteType,SubDepartment,SubDepartmentDescription,Class,ClassDescription,SubClass,SubClassDescription,MCDescription"

sed -i.bak "1 s/^.*$/$new_header/" INV.csv

