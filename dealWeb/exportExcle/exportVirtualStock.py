import pymysql
#import xlwt

import openpyxl

from openpyxl import Workbook



def export(date):

    # 打开数据库连接
    db = pymysql.connect("rdsd51v1a87ixlc6uu5uo.mysql.rds.aliyuncs.com","db_mamahao_root","db_mamahao_pwd_123987","db_gd")
    db_dev=pymysql.connect("rm-bp1ou9d6dch2hiy5jqo.mysql.rds.aliyuncs.com","db_read","ya0shur00Q","mamahao_warehouse" )

    wb = Workbook()
    ws=wb.active

    ws.title='sheet 1'


    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    cursor2=db_dev.cursor()

    # SQL 查询语句
    sql =" select b.BARCODE_1 as '条形码',c.sku_name as '品名',a.qty as '库存' from t_virtual_stock a "\
         " left join gb_share_item b on a.item_num_id=b.item_num_id "\
        " left join gb_share_item_ext c on a.item_num_id=c.item_num_id "\
        " where sid=1800000080 and virtual_stock_type=7 "

    result=["条形码","品名","库存"]
    ws.append(result)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        n=0
        for row in results:
            n=n+1
            row=list(row)
            ws.append(row)
    except Exception as e:
        print(str(e))
        print ("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    db_dev.close()
    wb.save('/Users/wangguannan/Downloads/虚拟仓库存.xlsx')

if __name__=="__main__":
        export("")