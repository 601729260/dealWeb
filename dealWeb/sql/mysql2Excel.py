
import pymysql

# 打开数据库连接
db = pymysql.connect("rdsd51v1a87ixlc6uu5uo.mysql.rds.aliyuncs.com","db_mamahao_root","db_mamahao_pwd_123987","db_gb" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM t_provider_info "
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()