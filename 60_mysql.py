import pymysql

__author__ = 'Lenovo'

# 建立连接
conn = pymysql.connect('localhost', 'root', '123456', 'movies', charset='utf8')

#建立游标
cursor = conn.cursor()

# crud
sql  = "insert into tb_user (name, pwd) values('dd','123456')"
sql = "delete from tb_user where id={0}".format(2)
sql = "update tb_user set pwd='123456' where name = 'dd'"
sql = 'select * from tb_user'

cursor.execute(sql)

result = cursor.fetchall()
print(result)

# 关闭游标和连接
cursor.close()
conn.close()