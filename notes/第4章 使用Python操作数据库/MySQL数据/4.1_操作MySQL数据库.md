# 操作MySQL数据库

---

结构化数据语言

用于管理文件的一个软件

主键：保证数据的唯一性，一个表只能有一个，可以是多列，不能重复也不能为空

```mysql
create database db2 default charset utf8;
show databases;
drop database db2;
truncate table tb1;  # 增序从1开始

show tables;
create table t1(id int,name char(10)) default charset=utf8;
select * from t1;
insert into t1(id,name) values(1,'egon');
```

外键：用数字代表表格中固定几类的内容，节省空间，并且约束该列里所填内容的格式及数字范围，表和表之间建立联系。

```mysql
create table userinfo(uid bigint auto_increment primary key,name varchar(32),department_id int,constraint fk_user_depar foreign key ("department_id,") references department("id"))

create table department(id bigint auto_increment primary key,title char(15))
```

```mysql
desc t10;
show create table t10 \G;
alter table auto_increment=20;
```

步长设置

```mysql
show session variables like 'auto_inc%';
set session auto_increment_increment=2;
show global variables like 'auto_inc%';
set global auto_increment_increment=2;
```

唯一索引：加速查找

`unique uq1 (num,xx)`约束不能重复，加速查找，可以为空

外键的变种

- 用户表和部门表

SQL语句操作补充

增删改查

```mysql
insert into tb(name,age) values('alex',18);
insert into tb(name,age) values('alex',18),('root',18);
insert into tb12(name,age) select name age from tb11;

delete from tb12 where id != 2 and name='alex';

update tb12 set name='alex',age=12 where id>12 and name = 'xx';

select id,name,11 as chame from tb12 where id > 10 or name = 'alex';
select * from tb12 where id in (1,4,12);
select * from tb12 where id between 5 and 12;
select * from tb12 where id in (select id in tb11);

select * from tb12 where name like "a%";
select * from tb12 where name like "a_";

select * from tb12 limit 10;
select * from tb12 limit 1,1; # 起始位置，向后取多少条
select * from tb12 limit 10 offset 20;

select * from tb12 order by id desc; # 从大到小
select * from tb12 order by id asc;

select max(id),part_id from tb12 group by part_id; # 分组
select count(id),part_id from tb12 group by part_id;
select count(id),part_id from tb12 group by part_id having count(id) > 1;  # 二次分组

select * from tb11,tb12 where tb11.part_id = tb12.id; # 连表操作
select * from tb11 left join tb12 on tb11.part_id = tb12.id; # 左边全部显示
```



```python
# Python实现用户登陆
# MySQL保存数据
import pymysql

user = input('username:')
pwd = input('password:')

conn = pymysql.connect(host='localhost_3306', user='root',password='582153',database='tb1')
cursor = conn.sursor()
# 连接数据库成功
sql = "select * from userinfo where username=%s and password=%s"
cursor.execute(sql,user,pwd)
result = cursor.fetchone()  # 只拿第一个
cursor.close()
conn.close()
print(result)

if result:
    print('登陆成功')
else:
    print('登陆失败')
```

```python
# 增加数据
user = 'eric'
pwd = '123123'
sql = "insert into userinfo(username,password) values(%s,%s)"
r = cursor.excutemany(sql,[(user,pwd),('egon','sb')])  # 受影响的行数
conn.commit()  # 修改时都需要
```

```python
# 查询时数据转换为字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 新插入数据的自增ID
cursor.lastrowid
```

join：左右连表

union：上下连表，自动去除重复，`union all`不去重

## 视图

给某个查询语句设置别名，日后方便使用，视图是虚拟的，不推荐使用

```mysql
# 创建视图
create view v1 as select * from student where sid > 10
alter view v1 as 
```

## 触发器

当对某张表做增删改时，可以使用触发器自定义关联行为

```mysql
delimiter //
create trigger t1 before insert on student for each row
BEGIN
insert into teacher(tname) values('sdf');
end
delimiter ;
```

## 函数

```mysql
select CURDATE();
select concat('a','b')
-- 时间格式

```

## 存储过程

保存在`MySQL`上的一个别名——一堆`SQL`语句

用来替代程序员写`SQL`语句

```mysql
-- 简单存储过程
delimiter //
create procedure p1()
begin
select * from student;
end
delimiter ;

```

特性：

可传参`in out inout`

`pymysql`

`out n2 int`用于标识存储过程的执行结果