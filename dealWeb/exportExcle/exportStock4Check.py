import pymysql
#import xlwt

import openpyxl

from openpyxl import Workbook



def export(ids):

    # 打开数据库连接
    db = pymysql.connect("rdsd51v1a87ixlc6uu5uo.mysql.rds.aliyuncs.com","db_mamahao_root","db_mamahao_pwd_123987","db_gd")
    db_dev=pymysql.connect("rm-bp1ou9d6dch2hiy5jqo.mysql.rds.aliyuncs.com","db_read","ya0shur00Q","mamahao_warehouse" )

    wb = Workbook()
    ws=wb.active

    ws.title='sheet 1'


    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    cursor2=db_dev.cursor()



    iddata="'"+("','").join(ids)+"'"

    # SQL 查询语句
    sql =" select shop.sub_unit_name as 门店,item_name as 品名 ,gb1.barcode_1 as 条码,a.qty as 库存 from t_gb_stock a "\
         " left join gb_share_item gb1 on a.item_num_id=gb1.item_num_id " \
         " left join gb_cort_sub_unit shop on a.shop_id=shop.sub_unit_num_id " \
         " where gb1.IS_DELETED=0 " \
         " and not exists(select 1 from u_stock_log_detail b where a.item_num_id=b.item_num_id and a.shop_id=b.to_sid  and b.id in("+iddata+"))"\
         " and a.shop_id in ("\
         " select to_sid  from u_stock_log where id in ("+iddata+"))"

    print(sql)


    result=["门店","品名","条码","库存"]
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
    wb.save('/Users/wangguannan/Downloads/无实物有库存记录.xlsx')

if __name__=="__main__":
    ids=[ "MMH2018120610012196","MMH2018120610012240","MMH2018120610012237","MMH2018120710012553"]
    export(ids)