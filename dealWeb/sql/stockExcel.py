import os

import xlrd
import string
data = xlrd.open_workbook('/Users/wangguannan/Downloads/万达店库存商品汇总.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows      # 获取表的行数
sql=''
header = 'insert into t_provider_info(provider_id ,	provider_name ,	linkman_name ,	contact_number,	bussiness_model_type,	clearing_type ,	clearng_cycle ,		opening_bank_name,		bank_account ,		bank_account_name ,		tax_account ,		provider_prv_name ,		provider_city_name ,		provider_area_name ,		provider_add, 		cooperate_status_name	)	values '

sql+=header
for i in range(nrows):   # 循环逐行打印
    if i <1: # 跳过一行
        continue
    sql+="\n"

    rowvalue=table.row_values(i)

    for j in range(0,23):
        rowvalue[j]="'"+str(rowvalue[j]).replace("\n","")+"'"


    value="("+",".join(rowvalue)+")"

    if i%1000==0 and i>0:
     value+=";\n"
     if i<nrows-1:
       sql+=header
    else:
     sql+=value+","


print(sql)

