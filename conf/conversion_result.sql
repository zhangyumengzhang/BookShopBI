--在Hive创建临时表
create table conversion_result(
  process STRING,
  counts INT,
  countu INT
) PARTITIONED BY(dt STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
