
import pymysql
import xlwt

# 打开数据库连接
db = pymysql.connect("rdsd51v1a87ixlc6uu5uo.mysql.rds.aliyuncs.com","db_mamahao_root","db_mamahao_pwd_123987","db_gd")

db_dev=pymysql.connect("rm-bp1ou9d6dch2hiy5jqo.mysql.rds.aliyuncs.com","db_read","ya0shur00Q","mamahao_warehouse" )


wbk = xlwt.Workbook()

sheet = wbk.add_sheet('sheet 1')


# 使用cursor()方法获取操作游标
cursor = db.cursor()

cursor2=db_dev.cursor()

# SQL 查询语句
sql = " SELECT DISTINCT "\
" b.id,"\
" barcode AS '条码',"\
" a.style_title AS '商品名称',"\
" CONVERT(sum(a.check_num),CHAR) AS '盘点数量'"\
" FROM"\
" u_stock_log_detail a"\
" LEFT JOIN u_stock_log b ON a.id = b.id" \
      " WHERE b.bill_type=5" \
      " AND b.create_time >= '2018-11-12 11:25:00'" \
      " AND b.create_time <= '2018-11-15 18:21:00'" \
      " group by a.id,a.item_num_id,a.style_title  "


sql2="select a.barcode,c.goods_shelf_code,b.store_place_code from t_store_place_goods_relation a,t_store_place b,t_goods_shelf c where a.store_place_id=b.store_place_id and b.goods_shelf_id=c.goods_shelf_id"

dict={}

result=["id","条码","商品名称","盘点数量","货架"]

for i in range(len(result)):
    sheet.write(0,i,result[i])

try:
    # 执行SQL语句
    cursor2.execute(sql2)
    # 获取所有记录列表
    results2 = cursor2.fetchall()
    for row in results2:
        row=list(row)
        dict[row[0]]=row[1]+"-"+row[2]
        #print(row)

except Exception as e:
    print(str(e))

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    n=0
    for row in results:
        n=n+1
        row=list(row)
        if row[1] in dict:
         row.append(dict[row[1]])
        else:
         row.append("")
        #print(row)
        for i in range(len(row)):
            if row[i] is not None:
             row[i]=str(row[i])
            else:
             row[i]=""
            sheet.write(n,i,row[i])
except Exception as e:
    print(str(e))
    print ("Error: unable to fetch data")

print(result)




# 关闭数据库连接
db.close()
db_dev.close()
wbk.save('/Users/wangguannan/Downloads/盘点信息.xls')