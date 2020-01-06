**1.pymysql**

安装pymysql:在命令行上执行pip install pymysql

**2.安装mysql**

我的版本是8.0.13

账户：root   密码:zmr19980518

**3.测试pymysql是否能用**


**4.pymysql的一些方法及参数说明**

  ·pymysql.connect()
    
    host(str)  mysql服务器地址
    port(int)  服务器端口号 
    user(str)  用户名
    password(str)  密码
    db(str)    数据库名称
    charset(str)  连接编码


  ·connection对象支持的方法

    cursor()     使用该连接创建并返回游标
    commit()     提交当前事务
    rollback()   回滚当前事务
    close()      关闭连接


  ·cursor对象支持的方法

    execute(op)      执行一个数据库的查询命令
    fetchone()       取得结果集的下一行
    fetchmany(size)  获取结果集的下几行
    fetchall()       获取结果集的所有行
    rowcount()       返回数据条数或影响行数
    close()          关闭游标对象


**5.数据库连接**

```
import pymysql

conn=pymysql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="zmr19980518",
    database="address",
    charset="utf8"
)
```




**6.实例：插入数据**

```
# 获取游标
myCursor = myConnect.cursor()

# 插入数据
myInsert = "insert into students(snum,sname,sage) values(%i,'%s','%s')"   # students是表名  snum,sname,sage是表属性
data1 = (3,"王五","19")
myCursor.execute(myInsert % data1)
myConnect.commit()
print("数据插入成功",myCursor.rowcount,'条数据')
```



================================================

参考：https://blog.csdn.net/iflytop/article/details/80934407










































