import os

import xlrd
import string
data = xlrd.open_workbook('/Users/wangguannan/Downloads/唯小宝商品供应商档案-供应商确认1030.xlsx') # 打开xls文件
table = data.sheets()[4] # 打开第一张表
nrows = table.nrows      # 获取表的行数
sql = 'insert into t_provider_info(provider_id ,	provider_name ,	linkman_name ,	contact_number,	bussiness_model_type,	clearing_type ,	clearng_cycle ,		opening_bank_name,		bank_account ,		bank_account_name ,		tax_account ,		provider_prv_name ,		provider_city_name ,		provider_area_name ,		provider_add, 		cooperate_status_name	)	values '
deletesql = 'delete from t_provider_info where provider_id in ( '
need=False

for i in range(nrows):   # 循环逐行打印
    if i <2: # 跳过两行
        continue
    rowvalue=table.row_values(i)
    if rowvalue[5]=="购销" :
        rowvalue[5]=1
    if rowvalue[5]=="代销" :
        rowvalue[5]=2
    if rowvalue[5]=="联营" :
        rowvalue[5]=3

    if rowvalue[6]=="预付款" :
        rowvalue[6]=1
    if rowvalue[6]=="月结" :
        rowvalue[6]=2
    if rowvalue[6]=="实销月结" :
        rowvalue[6]=3
    if rowvalue[6]=="票到" :
        rowvalue[6]=4
    if rowvalue[6]=="5货到" :
        rowvalue[6]=5

    if rowvalue[1]==None or rowvalue[1]=='':
        rowvalue[1]="nextval(\"provider_id\")"
    else:
        rowvalue[1]=int(rowvalue[1])
        if need==True :
            deletesql+=","
        deletesql+=str(rowvalue[1])
        need=True



    if  isinstance(rowvalue[7],float)!=True  and rowvalue[7].find("天"):
        rowvalue[7]=rowvalue[7].replace("天" ,"")
    else :
        rowvalue[7]=""

    for j in range(17):
        rowvalue[j]="'"+str(rowvalue[j]).replace("\n","")+"'"

    rowvalue=rowvalue[1:17]
    #print(",".join(rowvalue))
    if i<nrows-1:
        sql+="("+",".join(rowvalue)+"),\n"
    else:
        sql+="("+",".join(rowvalue)+");\n"

deletesql+=");"

sql=deletesql+"\n"+sql

print(sql)

#os.remove("/Users/wangguannan/Downloads/唯小宝商品供应商档案-供应商确认1030.sql")
fp = open("/Users/wangguannan/Downloads/唯小宝商品供应商档案-供应商确认1030.sql",'w')
fp.write(sql)
fp.close()
#if(table.row_values(i)(6)=="购销")
#print(table.row_values(i)[:13]) # 取前十三列