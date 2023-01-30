# sqoop导入hive建表

```sh
/opt/sqoop_1.4.7/bin/sqoop import \
-D mapred.job.queue.name=default \
-D mapred.task.timeout=0  \
-D org.apache.sqoop.splitter.allow_text_splitter=true --append \
--connect jdbc:mysql://host.docker.internal:3309/my_test \
--username root \
--password root \
--table pokemon \
--target-dir /home/big_data_selection/dim/dim_pokemon \
--fields-terminated-by '\t' \
--hive-drop-import-delims \
--input-null-string '\\N' \
--input-null-non-string '\\N' \
```

```sql
drop table dim_pokemon;
create table if not exists dim_pokemon
(
	name   string comment '姓名',
	hp     int comment 'hp',
	ack    int comment '攻击',
	def    int comment '防御',
	sp_ack int comment '特攻',
	sp_def int comment '特防',
	speed  int comment '速度'
)
	row format delimited fields terminated by '\t'
	stored as textfile
	location 'hdfs://namenode:8020/home/big_data_selection/dim/dim_pokemon';
msck repair table dim_pokemon;
```

