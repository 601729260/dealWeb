import os

import xlrd
import string


data = xlrd.open_workbook('/Users/wangguannan/Downloads/订单修改成本价(1).xlsx')
id='MMH2018111010003511'
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows      # 获取表的行数
sql=''
for i in range(nrows-1):   # 循环逐行打印
    if i <2: # 跳过两行
        continue


    rowlist=list(table.row_values(i))
    for i in range(len(rowlist)):
        rowlist[i]=str(rowlist[i])

    sql='update u_stock_log_detail set purchase_price='+rowlist[4]+',total_purchase_price='+rowlist[5]+' ,cost_price='+rowlist[6]+',total_cost_price='+rowlist[7]+' where id="'+id+'";'
    print(sql)






