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
 sql = " select c.sub_unit_name as '门店',a.shop_id as '门店ID',b.BARCODE_1 as '条形码',ext.sku_name as '品名',a.qty as '库存' from t_gb_stock_"+date+" a          " \
      " left join gb_share_item b on a.item_num_id=b.item_num_id and b.is_deleted=0                                                                                      " \
      " left join gb_share_item_ext ext on a.item_num_id=ext.item_num_id                                                                               " \
      " left join gb_cort_sub_unit c on a.shop_id=c.SUB_UNIT_NUM_ID                                                                                    " \
      " where a.shop_id!=0 union all                                                                                                                   " \
      " select c.storage_name as '门店',a.storage_id as '门店ID',b.BARCODE_1 as '条形码',ext.sku_name as '品名',a.qty as '库存' from t_gb_stock_"+date+" a        " \
      " left join gb_share_item b on a.item_num_id=b.item_num_id and b.is_deleted=0                                                                                        " \
      " left join gb_share_item_ext ext on a.item_num_id=ext.item_num_id                                                                               " \
      " left join gb_storage c on a.storage_id=c.storage_num_id                                                                                        " \
      " where a.storage_id!=0                                                                                                                         " ;
 result=["门店","门店ID","条形码","品名","库存"]
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
 wb.save('/Users/wangguannan/Downloads/备份库存'+date+'.xlsx')

if __name__=="__main__":
    dates=["20181201"]
    for date in dates:
        export(date)