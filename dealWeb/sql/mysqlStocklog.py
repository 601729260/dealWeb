

import pymysql

# 打开数据库连接
db = pymysql.connect("rdsd51v1a87ixlc6uu5uo.mysql.rds.aliyuncs.com","db_mamahao_root","db_mamahao_pwd_123987","db_gd" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

fileheader='/Users/wangguannan/Downloads/单据明细'
ID="MMH2018103110000395"

header="单据编号,商品货号,商品条码,商品名称,规格,剩余库存,申请调货数量,同意调货数量"
# SQL 查询语句
sql = "SELECT id AS '单据编号',style_code AS '商品货号',barcode AS '商品条码',style_title AS '商品名称',one_value AS '规格'," \
      "p_qty AS '剩余库存',apply_from_num AS '申请调货数量' ,from_num as '同意调货数量'FROM u_stock_log_detail WHERE id = '"+ID+"'";

data=header+"\n"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        row=list(row)
        for j in range(len(row)):
            row[j]=str(row[j]).replace("\"","\\\"")
        data+=",".join(row)+"\n"
        print(row)
except:
    print ("Error: unable to fetch data")




# 关闭数据库连接
db.close()

fp = open(fileheader+ID+".csv",'w')
fp.write(data)
fp.close()



