import pymysql
import xlrd
import os


fileheader='/Users/wangguannan/Downloads/库位11-9'

db = pymysql.connect("rdsd51v1a87ixlc6uu5uo.mysql.rds.aliyuncs.com","db_mamahao_root","db_mamahao_pwd_123987","db_gd")

data = xlrd.open_workbook(fileheader+".xlsx") # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows      # 获取表的行数


goodsshelfheader="insert into t_goods_shelf(sid,goods_shelf_id,goods_shelf_code,goods_shelf_name) values \n"
goodsshelfvalue=""

placeheader="insert into t_store_place(store_place_id,store_place_code,store_place_name,goods_shelf_id) values \n"
placevalue=""

relationheader="insert into t_store_place_goods_relation(item_num_id,style_num_id,style_id,style_title,barcode,unit_name,specifications,store_place_id) values"
relationvalue=""


need=False
need1=False
shelf_id=10000
store_place_id=10000

barcodes=[]
dict1={}
dict2={}
dict3={}

first=False

for i in range(nrows):   # 循环逐行打印
    if i <1: # 跳过一行
        continue
    rowvalue=table.row_values(i)

    if rowvalue[0].find("-") and rowvalue[0]!="":
     shelf_place=rowvalue[0].split("-")
     if len(shelf_place)==2:







        if shelf_place[0] not in dict2:
            if first==True:
                goodsshelfvalue+=",\n"
            shelf_id+=1
            goodsshelf=['1000000006',"'"+str(shelf_id)+"'","'"+str(shelf_place[0])+"'","'"+str(shelf_place[0])+"'"]
            dict2[shelf_place[0]]=shelf_id
            goodsshelfvalue+="("+",".join(goodsshelf)+")"


        if rowvalue[0] not in dict3:
            if first==True:
                placevalue+=",\n"
            store_place_id+=1
            storeplace=["'"+str(store_place_id)+"'","'"+str(shelf_place[1])+"'","'"+str(shelf_place[1])+"'","'"+str(dict2[shelf_place[0]])+"'"]
            placevalue+="("+",".join(storeplace)+")"
            dict3[rowvalue[0]]=store_place_id

        dict1[rowvalue[1]]=rowvalue[0]

        first=True

        barcodes.append(rowvalue[1])

        #print(goodsshelf)
        #print(storeplace)
        #print(relation)

goodsshelfvalue+=";\n"
placevalue+=";\n";

insertshelf=goodsshelfheader+goodsshelfvalue;

insertplace=placeheader+placevalue;

#-------------------查询数据
# 打开数据库连接

# 使用cursor()方法获取操作游标
cursor = db.cursor()

for i in range(len(barcodes)):
    barcodes[i]="'"+barcodes[i]+"'"
# SQL 查询语句
#sql = "	select item_num_id,a.style_num_id,c.STYLE_ID,c.style_title,barcode_1,b.unit, concat(a.color_name,'/',a.size_name) " \
#      "from gb_share_item a ,gb_style_ext b ,gb_style c" \
#      " where a.style_num_id=b.style_num_id " \
#      "and a.style_num_id=c.style_num_id and barcode_1 in ( " +",".join(barcodes)+");"


sql = "select item_num_id,a.style_num_id,c.STYLE_ID,c.style_title,barcode_1,b.unit, concat(a.color_name,'/',a.size_name)" \
      " from gb_share_item a ,gb_style_ext b ,gb_style c" \
      " where a.style_num_id=b.style_num_id" \
      " and a.style_num_id=c.style_num_id and a.item_num_id in (" \
      " select item_num_id from (" \
      " select item_num_id from gb_share_item where barcode_1 in  ( " +",".join(barcodes)+" ) order by online desc  ) t group by barcode_1 );"

insertrelation=""
rowvalue=[]
try:

    print(sql)

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    first=False
    k=0
    for row in results:
        k+=1
        row=list(row)
        row.append(str(dict3[dict1[row[4]]]))
        for j in range(len(row)):
            row[j]='"'+str(row[j]).replace("\"","\\\"")+'"'
        if first==True:
            relationvalue+=",\n"
        relationvalue+="("+",".join(row)+")"
        first=True
    relationvalue+=";\n"

    insertrelation=relationheader+relationvalue;

except Exception as e:
    print(str(e))
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()


filevalue=insertshelf+insertplace+insertrelation
print(filevalue)
os.remove(fileheader+".sql")
fp = open(fileheader+".sql",'w')
fp.write(filevalue)
fp.close()


