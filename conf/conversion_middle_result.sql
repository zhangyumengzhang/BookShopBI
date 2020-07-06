--在Hive创建临时表
create table conversion_middle_result(
  sessionid STRING,
  uuid STRING,
  process STRING
) PARTITIONED BY(dt STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
