--在Hive创建临时表
create table conversion_input(
  url STRING,
  uuid STRING,
  sessionId STRING,
  csvp INT
) PARTITIONED BY(dt STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
