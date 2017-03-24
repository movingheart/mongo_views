# 功能：
使用django基于HighChart展示mysql中的mongodb监控数据

# 函数
### 获取所有的库名：
1. 查找mysql表中的不同的mongo_base

### 获取某个库的所有集合名：
1. 根据库名mongo_base查找mysql表中不同的mongo_col

### 获取某个集合的100条记录数据
1. 根据库名和集合名获查找mysql表中100条数据


# 使用方法
1. 替换utils/settings.py中的配置为自己的参数
2. 新建mysql的库和表，并插入相关监控数据
3. 进入文件夹运行：python manage.py runserver 0.0.0.0:8000


# 依赖关系
* Python (2.7.11)
* Django (1.9.5)
* MySQL-python (1.2.3)
---
* jquery-1.8.3
* highcharts




# 作者
* 名称：alan wan
* 邮箱：movingheart000@gmail.com

# 时间
2017.03.24

# 数据字典：
1. 应用监控app_monitor_game、app_monitor_total

```sql
CREATE TABLE `handle_mongo` (
  `mongo_base` varchar(100) NOT NULL COMMENT 'mongo库名',
  `mongo_col` varchar(100) NOT NULL COMMENT 'mongo集合名',
  `update_count` int(11) DEFAULT NULL COMMENT '更新的记录数',
  `timestamp` datetime DEFAULT NULL COMMENT '插入时间',
  KEY `base_col` (`mongo_base`,`mongo_col`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
